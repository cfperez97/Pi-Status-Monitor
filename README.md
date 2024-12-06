# Pi-Status-Monitor
 A Python based status monitor and logger for the Raspberry Pi

 Please be sure to install all necessary packages on your Raspberry Pi. This script was tested on a Raspberry Pi 5. Some functionality may not work on other Raspberry Pi's.

 Help dialog:
```
 usage: status_monitor.py [-h] [-dw] [-nl] [seconds]

 Prints out to the console and logs various parameters.

 positional arguments:
   seconds            Additional seconds to wait between readings. Can accept an int or a float.

 optional arguments:
   -h, --help         show this help message and exit
   -dw, --dont_write  Don't constantly write to log after every reading.
   -nl, --no_labels   Don't write the labels of each column on the first line.
```
 Example output:
```
Date,Input Voltage,CPU Temp,CPU Clock,CPU Usage,Governor,Fan RPM,Fan Percent,Undervoltage detected,Arm frequency capped,Currently throttled,Soft temperature limit active,Undervoltage has occurred,Arm frequency capping has occurred,Throttling has occurred,Soft temperature limit has occurred
2024-11-21 21:01:25.863248,4.88832,47.7,1700027648,11.8,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:26.913180,4.8977,46.6,1500019456,0.2,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:27.974691,4.89234,46.6,1500019456,0.0,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:29.052134,4.89234,47.7,1500022656,0.5,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:30.131611,4.89234,46.6,1500012800,0.7,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:31.210061,4.8843,48.3,1500019456,1.4,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:32.284720,4.9044,47.7,1500012800,1.2,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:33.361643,4.89636,46.6,1500012800,0.9,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:34.441023,4.89234,48.8,1500016128,0.7,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:35.518896,4.90172,48.3,1500016128,0.9,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:36.594719,4.88832,47.7,1500019456,1.6,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:37.672264,4.89636,46.6,1500016128,0.9,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:38.750199,4.8977,46.6,1500016128,0.9,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:39.827477,4.89368,48.3,1500019456,1.2,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:40.903498,4.8977,46.6,1500012800,2.3,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:41.979943,4.90172,48.3,1500016128,0.9,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:43.057351,4.90038,48.8,1500019456,0.9,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:44.134435,4.88296,46.6,1500016128,1.2,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:45.213665,4.90172,46.1,1500016128,1.4,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:46.290815,4.90306,46.6,1500019456,1.4,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:47.367307,4.90038,47.2,1500012800,0.7,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:48.444204,4.9044,46.6,1500016128,1.2,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:49.521233,4.8977,47.7,1500009472,1.2,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:50.594385,4.8977,46.6,1500012800,1.2,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:51.671999,4.90842,47.7,1500012800,0.9,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:52.748714,4.90708,47.7,1500022656,1.2,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:53.825540,4.891,47.7,1500012800,1.2,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:54.902203,4.8977,47.7,1500019456,1.2,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:55.981119,4.89234,46.6,1500012800,0.9,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:57.062769,4.89368,47.7,1500019456,1.9,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:58.137143,4.89636,46.6,1500012800,1.2,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:01:59.213861,4.90038,47.7,1500019456,1.2,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:02:00.295345,4.8977,47.7,1500019456,1.1,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:02:01.376773,4.89368,47.7,1500022656,1.2,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:02:02.451457,4.8977,48.8,1500016128,2.1,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:02:03.534663,4.8441,49.4,2400023808,11.6,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:02:04.608224,4.88296,47.7,2400030464,1.8,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:02:05.717878,4.88832,47.7,2400027136,14.4,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:02:06.798797,4.88564,49.4,2400020480,6.1,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:02:07.870746,4.86286,47.7,1500016128,1.9,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:02:08.948793,4.891,49.4,1700017792,6.7,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:02:10.030446,4.88162,49.4,1500016128,3.9,ondemand,0,0,False,False,False,False,False,False,False,False
2024-11-21 21:02:11.114290,4.88832,48.3,2400017408,10.9,ondemand,5,75,False,False,False,False,False,False,False,False
2024-11-21 21:02:12.191578,4.86956,48.3,2400023808,2.8,ondemand,1095,75,False,False,False,False,False,False,False,False
2024-11-21 21:02:13.270390,4.86688,49.4,2400027136,1.6,ondemand,1194,75,False,False,False,False,False,False,False,False
2024-11-21 21:02:14.346411,4.88832,51.0,2400030464,1.2,ondemand,1207,75,False,False,False,False,False,False,False,False
2024-11-21 21:02:15.423812,4.88564,47.7,2400030464,1.2,ondemand,1209,75,False,False,False,False,False,False,False,False
2024-11-21 21:02:16.498703,4.88698,48.3,1600023552,4.4,ondemand,1210,75,False,False,False,False,False,False,False,False
2024-11-21 21:02:17.578818,4.88296,48.8,1600017024,4.0,ondemand,1210,75,False,False,False,False,False,False,False,False
2024-11-21 21:02:18.661076,4.89636,47.7,1500012800,4.2,ondemand,1210,75,False,False,False,False,False,False,False,False
2024-11-21 21:02:19.739957,4.86688,48.8,1800022016,7.3,ondemand,1211,75,False,False,False,False,False,False,False,False
2024-11-21 21:02:20.821136,4.891,49.4,1600023552,3.5,ondemand,1211,75,False,False,False,False,False,False,False,False
2024-11-21 21:02:21.901291,4.90306,48.3,1500019456,3.9,ondemand,1213,75,False,False,False,False,False,False,False,False
2024-11-21 21:02:22.978676,4.89904,48.3,1500019456,3.5,ondemand,1213,75,False,False,False,False,False,False,False,False
```