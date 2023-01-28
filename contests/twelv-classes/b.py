from copy import deepcopy
from sys import stdin


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
        l = []
        for i in range(len(self.mat)):
            tmp = []
            for j in range(len(self.mat[i])):
                tmp.append(self.mat[i][j] + new_mat.mat[i][j])
            l.append(tmp)
        return Matrix(l)

    def __mul__(self, a):
        l = []
        for i in range(len(self.mat)):
            tmp = []
            for j in range(len(self.mat[i])):
                tmp.append(self.mat[i][j] * a)
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


exec(stdin.read())
