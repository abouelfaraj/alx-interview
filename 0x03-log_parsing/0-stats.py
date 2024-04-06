#!/usr/bin/python3
"""
"""


import sys
import signal
from collections import defaultdict

statusCount = defaultdict(int)

total = 0

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

def print_stats():
    print("File size:", total)
    for code in sorted(statusCount.keys()):
        print(f"{code}: {statusCount[code]}")

signal.signal(signal.SIGINT, signal_handler)

for i, line in enumerate(sys.stdin):
    try:
        parts = line.strip().split()
        ip, date, _, status_code, file_size = part[0], parts[3][1:], parts[5], parts[8], int(parts[9])
        statusCount[status_code] += 1

        if (i + 1) % 10 == 0:
            print_stats
    except Exception as e:
        continue

print_stats()
