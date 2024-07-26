#!/usr/bin/python3
"""
    A module to validate UTF-8 encoding.
"""

from typing import Union

def validUTF8(data) -> Union[bool, None]:
    """
    Checks if the given data represents valid UTF-8 encoding.
    
    Args:
        data (list): A list of integers representing bytes.
        
    Returns:
        bool: True if data is valid UTF-8 encoding, False otherwise.
    """
    remaining_bytes = 0

    for byte in data:
        binary_rep = format(byte, '#010b')[-8:]

        if remaining_bytes == 0:
            if binary_rep.startswith('110'):
                remaining_bytes = 1
            elif binary_rep.startswith('1110'):
                remaining_bytes = 2
            elif binary_rep.startswith('11110'):
                remaining_bytes = 3
            elif binary_rep.startswith('10'):
                return False
        else:
            if not binary_rep.startswith('10'):
                return False
            remaining_bytes -= 1

    return remaining_bytes == 0
