#!/usr/bin/python3
"""Returns the peak in an array"""


def find_peak(landscape=[]):
    """peak function"""
    size = len(landscape)
    if size > 0:
        start, end = 0, len(landscape) - 1
        while start < end:
            mid = (start + end) // 2

            if (landscape[mid] < landscape[mid + 1]):
                start = mid + 1
            else:
                end = mid
        return landscape[start]

    return None
