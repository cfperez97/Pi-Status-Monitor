#!/usr/bin/python
from datetime import datetime
import csv
import time
from RaspberryPiVcgencmd import Vcgencmd

#sudo apt install stress
#stress --cpu 4

def retrieve_contents(file_name):
   try:
      with open(file_name) as f:
        return f.read().strip()
      
   except FileNotFoundError:
      return ''

def main():
    d = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
    with open(f"status_log_{d}.csv", mode='a+', newline='') as status_log:
        writer = csv.writer(status_log)
        vcgm = Vcgencmd()

        while True:
            date = datetime.now()
            temp = vcgm.measure_temp()
            clock = vcgm.measure_clock('arm')
            throttled = vcgm.get_throttled()['breakdown']
            gov = retrieve_contents('/sys/devices/system/cpu/cpufreq/policy0/scaling_governor')
            fan = retrieve_contents('/sys/devices/platform/cooling_fan/hwmon/hwmon2/fan1_input')
            pwm = retrieve_contents('/sys/devices/platform/cooling_fan/hwmon/hwmon2/pwm1')

            data = [date, temp, clock, *throttled.values(), gov, fan, pwm]

            print(data)
            writer.writerow(data)

            time.sleep(1)

if __name__ == '__main__':
    main()