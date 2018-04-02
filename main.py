#!/usr/bin/env python3

from matrix import *

import naive
import less_naive

import dp_recur

import numpy as np

import timeit
import string

def main():
    #less_naive_bench()
    #dp_recur_bench()
    #big_bench()
    assoc_test()

def basic_test():
    a = Mat.rand(10, 5)
    b = Mat.rand(5, 4)
    c = Mat.rand(4, 4)
    d = Mat.rand(4, 10)

    var = dict(a=a, b=b, c=c, d=d)

    seqs, count = naive.sequences(list(var.keys()))
    print("# of sequences: {}".format(len(seqs)))
    print("possible sequences:")

    for seq in seqs:
        mat = eval(seq, var)
        print("seq: {}, multiplies = {}".format(seq, mat.multiplies))

    print()

    best_seq, best_mat = naive.least_ops(list(seqs), var)
    print("optimal sequence: {}, multiplies = {}".format(best_seq, best_mat.ops()))
    print("time complexity: {}".format(count))

    print("result:")
    print(str(best_mat))
    print()

    print("numpy result:")
    a = np.matrix(a.mat)
    b = np.matrix(b.mat)
    c = np.matrix(c.mat)
    d = np.matrix(d.mat)

    print(a * b * c * d)

def naive_bench():
    print("NAIVE BENCH")

    for term_num in [2, 3, 4, 6, 8, 10]:
        letters = string.ascii_lowercase[:term_num]
        seqs, count = naive.sequences([ch for ch in letters])

        print("{}\t{}\t{}".format(term_num, count, len(seqs)))

def less_naive_bench():
    a = Mat.rand(10, 5)
    b = Mat.rand(5, 4)
    c = Mat.rand(4, 20)
    d = Mat.rand(20, 10)
    e = Mat.rand(10, 5)

    mats = [a.size(), b.size(), c.size(), d.size(), e.size()]
    var = [ch for ch in string.ascii_lowercase[:len(mats)]]
    var_dict = dict(a=a, b=b, c=c, d=d, e=e)

    cost, expr, count = less_naive.min_cost(mats, var)
    print("cheapest: {} <- {}".format(cost, expr))
    print("complexity: {}".format(count))

    seqs, count = naive.sequences(var)
    best_seq, best_mat = naive.least_ops(list(seqs), var_dict)

    print("actual: {} <- {}".format(best_mat.multiplies, best_seq))
    print("complexity: {}".format(count + len(seqs)))

    for seq in seqs:
        mat = eval(seq, var_dict)
        print("not optimal: {} <- {}".format(mat.multiplies, seq))

def dp_recur_bench():
    a = Mat.rand(10, 5)
    b = Mat.rand(5, 4)
    c = Mat.rand(4, 20)
    d = Mat.rand(20, 10)
    e = Mat.rand(10, 5)

    mats = [a.size(), b.size(), c.size(), d.size(), e.size()]
    var = [ch for ch in string.ascii_lowercase[:len(mats)]]
    var_dict = dict(a=a, b=b, c=c, d=d, e=e)

    cost, expr, count = dp_recur.min_cost(mats, var)
    print("cheapest: {} <- {}".format(cost, expr))
    print("complexity: {}".format(count))

    seqs, count = naive.sequences(var)
    best_seq, best_mat = naive.least_ops(list(seqs), var_dict)

    print("actual: {} <- {}".format(best_mat.multiplies, best_seq))
    print("complexity: {}".format(count + len(seqs)))

    for seq in seqs:
        mat = eval(seq, var_dict)
        print("not optimal: {} <- {}".format(mat.multiplies, seq))

def big_bench():
    mats = [
        Mat.rand(100, 500),
        Mat.rand(500, 40),
        Mat.rand(40, 200),
        Mat.rand(200, 100),
        Mat.rand(100, 4),
        Mat.rand(4, 20),
        Mat.rand(20, 250),
        Mat.rand(250, 100),
        Mat.rand(100, 5),
        Mat.rand(5, 40),
    ]

    var_names = [ch for ch in string.ascii_lowercase[:len(mats)]]
    var = { name : mats[i] for i, name in enumerate(var_names) }

    mat_sizes = [mat.size() for mat in mats]

    cost, expr, count = dp_recur.min_cost(mat_sizes, var_names)
    print("BEST:")
    print("({}) {}".format(cost, expr))
    
    result = eval(expr, var)
    print("Actual multiplies: {}".format(result.multiplies))

    expr_naive = "*".join(var_names)
    cur_mat = eval(expr_naive, var)

    print("Standard multiplies: {}".format(cur_mat.multiplies))
    print("Saving: {}".format(cost / cur_mat.multiplies))    

    t_fast = timeit.timeit(lambda: eval(expr, var), number=5)
    t_slow = timeit.timeit(lambda: eval(expr_naive, var), number=5)

    print("Time fast: {}, time slow: {}".format(t_fast, t_slow))

    seqs, count = naive.sequences(var_names)
    best_seq, best_mat = naive.least_ops(list(seqs), var)

    print("Sanity: {}".format(best_mat.multiplies))

def assoc_test():
    a = Mat.rand(10, 5)
    b = Mat.rand(5, 4)
    c = Mat.rand(4, 4)

    r1 = a * (b * c)
    r2 = (a * b) * c

    print("r1 = {}, r2 = {}".format(r1.multiplies, r2.multiplies))
    
if __name__ == "__main__":
    main()
