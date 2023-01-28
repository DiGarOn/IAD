from copy import deepcopy
from sys import stdin
from functools import singledispatchmethod


class MatrixError(Exception):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, new_list: list):
        self.mat = deepcopy(new_list)

    def __str__(self):
        res = ""
        for i in range(len(self.mat)):
            for j in range(len(self.mat[i])):
                res += str(self.mat[i][j])
                if j != len(self.mat[i]) - 1:
                    res += '\t'
            if i != len(self.mat) - 1:
                res += '\n'
        return res

    def size(self):
        if len(self.mat) != 0:
            return len(self.mat), len(self.mat[0])
        else:
            return 0, 0

    def __add__(self, new_mat):
        if len(self.mat) != len(new_mat.mat) or len(self.mat[0]) != len(new_mat.mat[0]):
            raise MatrixError(self, new_mat)

        l = []
        for i in range(len(self.mat)):
            tmp = []
            for j in range(len(self.mat[i])):
                tmp.append(self.mat[i][j] + new_mat.mat[i][j])
            l.append(tmp)
        return Matrix(l)

    @singledispatchmethod
    def __mul__(self, a: [int, float]):
        l = []
        for i in range(len(self.mat)):
            tmp = []
            for j in range(len(self.mat[i])):
                tmp.append(self.mat[i][j] * a)
            l.append(tmp)
        return Matrix(l)


    def __mul__(self, new_mat):
        if len(self.mat) != len(new_mat.mat[0]):
            raise MatrixError(self, new_mat)

        l = []
        for i in range(len(self.mat)):
            tmp = []
            for j in range(len(self.mat)):
                s = 0
                for k in range(len(self.mat[i])):
                     s += self.mat[i][k] * new_mat.mat[k][j]
                tmp.append(s)
            l.append(tmp)
        return Matrix(l)


    def __rmul__(self, a):
        l = []
        for i in range(len(self.mat)):
            tmp = []
            for j in range(len(self.mat[i])):
                tmp.append(self.mat[i][j] * a)
            l.append(tmp)
        return Matrix(l)

    def transpose(self):
        l1 = []
        for i in range(len(self.mat[0])):
            tmp = []
            for j in range(len(self.mat)):
                tmp.append(self.mat[j][i])
            l1.append(tmp)
        self.mat = deepcopy(l1)
        return self

    @staticmethod
    def transposed(new_mat):
        l1 = []
        for i in range(len(new_mat.mat[0])):
            tmp = []
            for j in range(len(new_mat.mat)):
                tmp.append(new_mat.mat[j][i])
            l1.append(tmp)
        return Matrix(l1)


# Task 4 check 3
mid = Matrix([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
print(5 * m2)
print(m2 * (120 * mid * m1))


# exec(stdin.read())
