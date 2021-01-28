#!/usr/bin/env python3
import argparse
from datetime import datetime, timedelta
from time import sleep
import os
import subprocess

parser = argparse.ArgumentParser(prog='remind', description='Make a remind')
parser.add_argument('-f', '--full_dt', action='store_true', help='enable the full date format')
parser.add_argument("time", help="time in format: H:M:S, if -f then Y:m:d:H:M:S ")
parser.add_argument("message", help="warning message", nargs='+')
args = parser.parse_args()
if args.full_dt:
    time = datetime.strptime(args.time, '%Y:%m:%d:%H:%M:%S')
else:
    time = datetime.strptime(args.time, '%H:%M')
    time = datetime.now().replace(hour=time.hour, minute=time.minute, second=0, microsecond=0)


if time < datetime.now():

    time += timedelta(days=1)

sleep_time: timedelta = time - datetime.now()
sleep_seconds: float = sleep_time.total_seconds()
path =__file__[:-9] + 'actual_remind.py'
print(__file__)
subprocess.call(['python', path, str(sleep_seconds), *args.message, '&'])
