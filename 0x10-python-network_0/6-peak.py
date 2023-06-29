#!/bin/python3
"""Returns the peak in an array"""


def find_peak(landscape):
    """peak function"""
    if len(landscape) == 0:
        return None
    elif len(landscape) == 1:
        return landscape[0]
    peak = landscape[0]
    i = 0
    for scape in landscape:
        if landscape[i] < landscape[i + 1]:
            if landscape[i + 1] == landscape[i + 2]:
                break
            peak = landscape[i + 1]
        elif landscape[i] == landscape[i + 1]:
            break
        else:
            if i > 0 and landscape[i] > landscape[i - 1]:
                break
        i += 1
    return peak
