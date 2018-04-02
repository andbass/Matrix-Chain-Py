
import random

class Mat:
    def __init__(self, mat, multiplies=0):
        self.mat = mat
        self.multiplies = multiplies

        self.rows = len(mat)
        self.cols = len(mat[0])

    def ident(n):
        """
        Creates a n X n identity matrix
        """
        mat = []
        for i in range(n):
            row = [0] * n
            row[i] = 1
        
            mat.append(row)

        return Mat(mat)

    def rand(m, n, lower=1, upper=10):
        """
        Creates a random m X n matrix, with entries as integers from [`lower`, `upper`], inclusive
        """
        mat = []
        for _ in range(m):
            row = [int(random.uniform(lower, upper)) for _ in range(n)]
            mat.append(row)

        return Mat(mat)

    def size(self):
        """
        Returns the size of matrix `a`, with element [0] being the rows, and [1] being the columns
        """
        return [self.rows, self.cols]

    def ops(self):
        """
        Returns number of multiplies needed to compute matrix
        Factors in multiplies from previous multiplications
        """
        return self.multiplies

    def can_mul(self, rhs):
        return self.cols == rhs.rows

    def __mul__(self, rhs):
        assert self.can_mul(rhs)

        result_rows = self.rows
        result_cols = rhs.cols

        vec_len = self.cols

        multiplies = self.multiplies + rhs.multiplies
        mat = []

        for i in range(result_rows):
            row = []

            for j in range(result_cols):
                elem = 0
                for k in range(vec_len):
                    elem += self.mat[i][k] * rhs.mat[k][j]
                    multiplies += 1

                row.append(elem)
            mat.append(row)

        return Mat(mat, multiplies)

    __rmul__ = __mul__

    def __str__(self):
        """
        Converts a matrix `a` into a readable string
        """
        return "\n".join([str(row) for row in self.mat])

def mul_ops(a, b):
    """
    Computes the number of multiplies needed to multiply together matrices `a` and `b`
    Sizes are given as arrays, [0] are rows, and [1] are cols
    """
    assert a[1] == b[0]
    return a[0] * a[1] * b[1]

