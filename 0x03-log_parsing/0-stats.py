#!/usr/bin/python3

"""
    CODE DOCUMENTATIONS
    VERY USEFUL CODE
"""

import sys
import re
from collections import defaultdict

def print_stats(total_size, status_codes):
    """ PRINT STATS """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def parse_line(line):
    """ PARSE LINE """
    pattern = r'^(\S+) - \[(.+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
    match = re.match(pattern, line)
    if match:
        ip, date, status, file_size = match.groups()
        return int(status), int(file_size)
    return None, None

def main():
    """ MAIN FUNCTION """
    total_size = 0
    line_count = 0
    status_codes = defaultdict(int)

    try:
        for line in sys.stdin:
            status, file_size = parse_line(line.strip())
            if status is not None and file_size is not None:
                total_size += file_size
                status_codes[status] += 1
                line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
