#!/usr/bin/python3

"""
    STATs
"""

import sys
import re
import signal

def print_statistics(total_size, status_codes):
    """ Print statistics """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """ Handle CTRL+C """
    print_statistics(total_size, status_codes)
    sys.exit(0)

def main():
    """ Main function """
    global total_size, status_codes
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    # Set up signal handling
    signal.signal(signal.SIGINT, signal_handler)

    pattern = r'^\S+ - \[.+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'

    for line in sys.stdin:
        try:
            match = re.match(pattern, line.strip())
            if match:
                status_code = int(match.group(1))
                file_size = int(match.group(2))
                
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(total_size, status_codes)

        except KeyboardInterrupt:
            # This should not be needed due to signal handling, but kept for safety
            break
        except:
            # Skip lines that don't match the expected format
            continue

    # Print final statistics
    print_statistics(total_size, status_codes)

if __name__ == "__main__":
    main()