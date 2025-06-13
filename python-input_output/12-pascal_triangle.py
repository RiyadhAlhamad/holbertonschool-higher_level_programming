
#!/usr/bin/python3
"""
Module that contains pascal_triangle function
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n

    Args:
        n (int): number of rows in Pascal's triangle

    Returns:
        list: list of lists containing Pascal's triangle
              empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]

        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        triangle.append(row)
    return triangle
