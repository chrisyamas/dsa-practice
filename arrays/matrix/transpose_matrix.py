# LeetCode Problem
# Given a 2D integer array matrix, return the transpose of matrix.
#
# The transpose of a matrix is the matrix flipped over its main diagonal,
# switching the matrix's row and column indices.


# My solution:
def transpose(matrix):
    trans = [[] for x in matrix[0]]
    i = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans[j].append(matrix[i][j])
    return trans

    # Alternative LeetCode solution, simply:
    # return zip(*matrix)
