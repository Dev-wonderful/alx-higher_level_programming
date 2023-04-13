#!/usr/bin/python3

"""A module to create pascal's triangle"""


def pascal_triangle(n):
    """creates a pascal triangle"""
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        if len(triangle) == 0:
            row = [1]
            triangle.append(row)
        else:
            row = []
            pre = triangle[i-1]
            for j in range(len(pre)):
                if j == 0:
                    row.append(pre[j])
                if j + 1 < len(pre):
                    x = pre[j+1] + pre[j]
                    row.append(x)
                elif j + 1 == len(pre):
                    row.append(pre[j])
            triangle.append(row)
    return triangle
