import random
n = 10
matrix = [[[random.randrange(0, 9) for k in xrange(n)] for j in xrange(n)] for i in xrange(n)]

def max_coord(matrix):
    max_sum = 0
    max_z,max_x,max_y = 0,0,0
    for z in range(0, len(matrix)):
        for x in range(0, len(matrix[z])):
            for y in range(0, len(matrix[z][x])):
                sum_z=sum([matrix[i][x][y] for i in range(0,len(matrix))])
                sum_x=sum([matrix[z][i][y] for i in range(0,len(matrix[z]))])
                sum_y=sum([matrix[z][x][i] for i in range(0,len(matrix[z][x]))])
                value_sum = sum_z + sum_y + sum_x - 2*(matrix[z][x][y])
                if value_sum > max_sum:
                    max_sum = value_sum
                    max_z,max_x,max_y = z,x,y
    return (max_z,max_x,max_y,max_sum)
result = max_coord(matrix)
print 'Maximum sum value: %s Coordinates: %s' % (result[3], result[0:3],)