#!/usr/bin/python3

"""
    A Python script that reads stdin
    line by line and computes metrics.
"""

import sys
import re
from collections import defaultdict


def print_stats(total_size, status_codes):
    """Print the accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """Parse a single line of log input."""
    pattern = (
        r'(\d+\.\d+\.\d+\.\d+) - '
        r'\[(.*?)\] '
        r'"GET /projects/260 HTTP/1.1" '
        r'(\d+) (\d+)'
    )
    match = re.match(pattern, line)
    if match:
        return int(match.group(3)), int(match.group(4))
    return None, None


def main():
    """Main function to process stdin and compute metrics."""
    total_size = 0
    line_count = 0
    status_codes = defaultdict(int)

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line.strip())
            if status_code and file_size:
                total_size += file_size
                status_codes[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # Handle CTRL+C interrupt
        print_stats(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
