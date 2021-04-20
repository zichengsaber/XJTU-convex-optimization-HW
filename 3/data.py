import numpy 

# 创造矩阵A


def creat_A(p, n):
    return numpy.random.random(size=(p, n))

# 创造可行解x


def creat_x(n):
    return numpy.random.random(size=(n, 1))


if __name__ == '__main__':
    # 保证A是行满秩
    numpy.random.seed(0)
    A = creat_A(30, 100)
    while numpy.linalg.matrix_rank(A) != 30:
        A = creat_A(30, 100)
    x_can = creat_x(100)
    b = numpy.dot(A, x_can)
    numpy.savetxt('A.txt', A)
    numpy.savetxt('x_can.txt', x_can)
    numpy.savetxt('b.txt', b)
