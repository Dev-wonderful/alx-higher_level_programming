#!/usr/bin/python3
"""Returns the peak in an array"""


def find_peak(landscape=[]):
    """peak function"""
    if len(landscape) == 0:
        return None
    elif len(landscape) == 1:
        return landscape[0]
    peak = landscape[0]
    i = 1
    while i < len(landscape):
        prev = landscape[i - 1]
        curr = landscape[i]
        if len(landscape) > i + 1:
            next_el = landscape[i + 1]
        if curr > prev and curr > next_el:
            peak = curr
            return peak
        if curr == next_el and next_el <= peak:
            break
        elif curr == next_el and next_el > peak:
            return next_el
        i += 1
    return peak
