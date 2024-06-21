#!/usr/bin/python3
"""Module to find a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    start, end = 0, len(list_of_integers) - 1
    while start < end:
        mid = (start + end) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            start = mid + 1
        else:
            end = mid
    return list_of_integers[start]
