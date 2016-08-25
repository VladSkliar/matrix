import random
n = 3
distance = [[[random.randrange(0, 9) for k in xrange(n)] for j in xrange(n)] for i in xrange(n)]


def matrix_z_sum(matrix):
    sum_matrix = [[0 for k in xrange(n)] for j in xrange(n)]
    for i in range(0, len(matrix)):
        for z in range(0, len(matrix[i])):
            for j in range(0, len(matrix[i][z])):
                sum_matrix[z][j] += matrix[i][z][j]
    return sum_matrix


def sum_in_matrix(matrix):
    sum_matrix = [[[0 for k in xrange(n)] for j in xrange(n)] for i in xrange(n)]
    for i in range(0, len(matrix)):
        for z in range(0, len(matrix[i])):
            for j in range(0, len(matrix[i][z])):
                x = sum(matrix[i][z])
                for v in range(0, len(matrix[i])):
                    x += matrix[i][v][j]
                x -= matrix[i][z][j]
                sum_matrix[i][z][j] += x
    return sum_matrix


def final(sum_in_matrix, sum_z, native_matrix):
    max_num = 0
    max_i = 0
    max_j = 0
    max_z = 0
    for i in range(0, len(sum_in_matrix)):
        for z in range(0, len(sum_in_matrix[i])):
            for j in range(0, len(sum_in_matrix[i][z])):
                value = sum_in_matrix[i][z][j] - native_matrix[i][z][j] + sum_z[z][j]
                if value > max_num:
                    max_num = value
                    max_z = z
                    max_j = j
                    max_i = i
    print(max_i, max_z, max_j, max_num)

sum_z = matrix_z_sum(distance)
sum_in_matrix = sum_in_matrix(distance)

final(sum_in_matrix, sum_z, distance)
