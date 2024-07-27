#!/usr/bin/python3
'''
Write a method that determines if a given data set represents a valid
UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to
handle the 8 least significant bits of each integer
'''


def validUTF8(data):
    '''
    Check if data is valid utf-8

    Notes:
    1- The leading byte are: 0xxxxxxx, 110xxxxx, 1110xxxx and 11110xxx
    2- The continuation byte is 10xxxxxx
    '''

    bytes_count = 0
    for byte in data:

        if bytes_count == 0:
            # Check for 1-byte character 0xxxxxxx
            if (byte & 0b10000000) == 0b00000000:
                continue

            # Check for 2-bytes character 110xxxxx
            elif (byte & 0b11100000) == 0b11000000:
                bytes_count = 1

            # Check for 3-bytes character 1110xxxx
            elif (byte & 0b11110000) == 0b11100000:
                bytes_count = 2

            # Check for 4-bytes character 11110xxx
            elif (byte & 0b11111000) == 0b11110000:
                bytes_count = 3

            else:
                return False
        else:
            if not is_continuation_byte(byte):
                return False
            bytes_count -= 1

    return bytes_count == 0


def is_continuation_byte(byte):
    '''
    Check if byte is valid continuation byte in utf-8
    '''
    return (byte & 0b11000000) == 0b10000000
