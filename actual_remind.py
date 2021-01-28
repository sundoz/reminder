#!/usr/bin/env python3
import sys
import time

args = sys.argv

time.sleep(float(args[1]))
for i in range(10):
    print('\a')
    time.sleep(0.5)
print(*args[2:])

