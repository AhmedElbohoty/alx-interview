#!/usr/bin/python3
'''
script that reads stdin line by line and computes metrics:
'''
import sys

status_code = [200, 301, 400, 401, 403, 404, 405, 500]
log = {'file_size': 0, 'code_list': {str(code): 0 for code in status_code}}


def parse_line(line):
    '''Parse line'''
    items = line.split()

    try:
        size = items[-1]
        log['file_size'] += int(size)

        code = items[-2]
        if int(code) in status_code:
            log['code_list'][code] += 1

    except Exception:
        pass


def print_codes():
    '''Print codes'''
    print("File size: {:d}".format(log['file_size']), flush=True)

    sorted_codes = sorted(log['code_list'])
    for code in sorted_codes:
        count = log['code_list'][code]
        if count > 0:
            print("{:s}: {:d}".format(code, count), flush=True)


def main():
    '''
    The main function
    '''
    count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            count += 1
            parse_line(line)

            if count % 10 == 0:
                print_codes()
                count = 0
        print_codes()
    except (KeyboardInterrupt, EOFError):
        print_codes()


if __name__ == "__main__":
    main()
