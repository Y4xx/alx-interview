#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """
    pascal_triangle
    """
    list_list = []
    if n > 0:
        list_list.append([1])
        for i in range(1, n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = list_list[i - 1][j] + list_list[i - 1][j - 1]
            list_list.append(row)
    return list_list
