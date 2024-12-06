#!/home/gregoryreis/status_monitor/venv/bin/python

import argparse, csv, time, psutil, os, subprocess
from datetime import datetime
from vcgencmd import Vcgencmd

def retrieve_contents(file_name):
   try:
      with open(file_name) as f:
        return f.read().strip()
      
   except FileNotFoundError:
        return ''
   
def retrieve_int(file_name):
   try:
        return int(retrieve_contents(file_name))
      
   except TypeError:
        return 0

def main():
    parser = argparse.ArgumentParser(
             description='Prints out to the console and logs various parameters.')
    
    parser.add_argument('-dw', '--dont_write', action='store_true', 
                        help="Don't constantly write to log after every reading.")
    
    parser.add_argument('-nl', '--no_labels', action='store_true', 
                        help="Don't write the labels of each column on the first line.")
    
    parser.add_argument('seconds', nargs='?', default=1, type=float, 
                        help='Additional seconds to wait between readings. Can accept an int or a float.')

    try:
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        print('Error parsing arguments:', e)
        parser.print_help()
        exit(1)

    d = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
    with open(f"/home/gregoryreis/status_monitor/status_log_{d}.csv", mode='a+', newline='') as status_log:
        writer = csv.writer(status_log)
        vcgm = Vcgencmd()
        
        # gets rid of the first value that is always 0
        _ = psutil.cpu_percent(percpu=False)
        
        labels = ['Date', 'Input Voltage', 'CPU Temp', 'CPU Clock', 'CPU Usage', 'Governor', 'Fan RPM', 'Fan Percent',
                  'Undervoltage detected', 'Arm frequency capped', 'Currently throttled', 'Soft temperature limit active',
                  'Undervoltage has occurred', 'Arm frequency capping has occurred', 'Throttling has occurred',
                  'Soft temperature limit has occurred', ]

        if not args.no_labels:
            print(labels)
            writer.writerow(labels)
        
        while True:
            date = datetime.now()
            pmic_read_adc = subprocess.run(['vcgencmd', 'pmic_read_adc'], capture_output=True, text=True)
            input_voltage = float(pmic_read_adc.stdout[864:874])
            cpu_temp = vcgm.measure_temp()
            cpu_clock = vcgm.measure_clock('arm')
            cpu_usage = psutil.cpu_percent(percpu=False)
            governor = retrieve_contents('/sys/devices/system/cpu/cpufreq/policy0/scaling_governor')
            fan_rpm = retrieve_int('/sys/devices/platform/cooling_fan/hwmon/hwmon2/fan1_input')
            fan_percent = retrieve_int('/sys/devices/platform/cooling_fan/hwmon/hwmon2/pwm1')
            throttled = vcgm.get_throttled()['breakdown']

            data = [date, input_voltage, cpu_temp, cpu_clock, cpu_usage, governor, fan_rpm, fan_percent, *throttled.values(), ]

            print(data)
            writer.writerow(data)
            
            if not args.dont_write:
                status_log.flush()
                os.fsync(status_log.fileno())

            time.sleep(args.seconds)

if __name__ == '__main__':
    main()
