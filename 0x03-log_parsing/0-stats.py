#!/usr/bin/python3
'''
script that reads stdin line by line and computes metrics:
'''
import sys
import re
import signal

status_code = [200, 301, 400, 401, 403, 404, 405, 500]
log = {'file_size': 0, 'code_list': {str(code): 0 for code in status_code}}


pattern = re.compile(
    # <IP Address>
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \['
    # [<date>] "GET /projects/260 HTTP/1.1"
    r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" '
    # <status code> <file size>
    r'(.{3}) (\d+)')


def parse_line(line):
    '''Parse line'''
    # Use fullmatch to match the whole line
    match = pattern.fullmatch(line)

    if match:
        code = match.group(1)
        size = match.group(2)

        log['file_size'] += int(size)
        if code.isdecimal():
            log['code_list'][code] += 1


def print_codes():
    '''Print codes'''
    print(f"File size: {log['file_size']}")

    sorted_codes = sorted(log['code_list'])
    for code in sorted_codes:
        count = log['code_list'][code]
        if count:
            print(f"{code}: {count}")


def signal_handler():
    '''Handle '''
    print_codes()
    sys.exit(0)


def main():
    '''
    The main function
    '''
    signal.signal(signal.SIGINT, signal_handler)

    count = 0

    for line in sys.stdin:
        line = line.strip()
        count += 1
        parse_line(line)

        if count == 10:
            print_codes()
            count = 0


if __name__ == "__main__":
    main()
