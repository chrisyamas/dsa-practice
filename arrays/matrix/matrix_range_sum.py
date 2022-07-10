"""
Given a matrix (2-D array) of integers and four non-negative integers
(corresponding to the top-left and bottom-right row and column indices,
respectively, of a sub-matrix of the input matrix) create a range-sum matrix
of the full input matrix and use it to return the range-sum of the sub-matrix.

The range-sum matrix is defined as a matrix where each element is equal to the
sum of all the elements with lesser indices in the same row in the original
matrix.

The range-sum is defined as the sum of all integers contained in (sub-)matrix.

Example:

example_matrix = [
[1, 2, 3],
[1, 2, 1],
[0, 1, 2],
]

example_range_sum_matrix = [
[1, 3, 6],
[1, 3, 4],
[0, 1, 3]
]

example_coords1 = [0, 0, 1, 1] --> 6
example_coords2 = [0, 0, 2, 2] --> 13
example_coords3 = [1, 1, 2, 2] --> 7
"""


def get_range_sum_matrix(matrix):
    range_sum_matrix = [[] for x in matrix]
    for i in range(len(matrix)):
        int_sum = 0
        for j in range(len(matrix[0])):
            int_sum += matrix[i][j]
            range_sum_matrix[i].append(int_sum)
    for x in range_sum_matrix:
        print(x)
    return range_sum_matrix


def convert_matrix_to_range_sum(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            current = matrix[i][j]
            if j == 0:
                int_sum = current
            else:
                int_sum = current + matrix[i][j - 1][1]
            matrix[i][j] = [current, int_sum]
    for x in matrix:
        print(x)


def get_sub_matrix_range_sum(matrix, coords):
    """
    coords = [0, 1, 1, 2] means that:
    - top-left (coords[0], coords[1]) is row0, col1
    - bottom-right (coords[2], coords[3]) is row1, col2
    """
    included = 0
    excluded = 0
    for i in range(coords[0], coords[2] + 1):
        if coords[1] > 0:
            excluded += matrix[i][coords[1] - 1]
        included += matrix[i][coords[3]]
    return included - excluded


if __name__ == '__main__':
    example_matrix = [
        [1, 2, 3],
        [1, 2, 1],
        [0, 1, 2],
    ]
    print(example_matrix)
    range_sum_matrix = get_range_sum_matrix(example_matrix)
    coordinates = [1, 1, 2, 2]
    result = get_sub_matrix_range_sum(range_sum_matrix, coordinates)
    print(result)
