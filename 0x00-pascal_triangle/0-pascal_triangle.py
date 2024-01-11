#!/usr/bin/env python3
"""0-pascal_triangle module"""
from typing import List


def pascal_triangle(n):
    """
    Generate Pascal's Triangle for n rows.
    """

    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
