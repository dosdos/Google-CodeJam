"""
Created on 05/apr/2014

@author: david

Problem A. Minimum Scalar Product
(https://code.google.com/codejam/contest/32016/dashboard#s=p0)


***Problem***

You are given two vectors v1=(x1,x2,...,xn) and v2=(y1,y2,...,yn).
The scalar product of these vectors is a single number, calculated as x1y1+x2y2+...+xnyn.

Suppose you are allowed to permute the coordinates of each vector as you wish.
hoose two permutations such that the scalar product of your two new vectors is the
smallest possible, and output that minimum scalar product.

***Input***

The first line of the input file contains integer number T - the number of test cases.
For each test case, the first line contains integer number n.
The next two lines contain n integers each, giving the coordinates of v1 and v2 respectively.

***Output***

For each test case, output a line

Case #X: Y
where X is the test case number, starting from 1, and Y is the minimum scalar product of
all permutations of the two given vectors.

***Limits***

**Small dataset**

T = 1000
1 ≤ n ≤ 8
-1000 ≤ xi, yi ≤ 1000

**Large dataset**

T = 10
100 ≤ n ≤ 800
-100000 ≤ xi, yi ≤ 100000

***Sample***

Input
2
3
1 3 -5
-2 4 1
5
1 2 3 4 5
1 0 1 0 1

Output
Case #1: -25
Case #2: 6


"""
__author__ = 'david'

import unittest


class MinimumScalarProduct(object):

    def __init__(self, input_file_name=None, output_file_name=None):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name

    # file I/O
    def read_word(self, file):
        return next(file).strip()

    def read_int(self, file, b=10):
        return int(self.read_word(file), b)

    def read_words(self, file, d=' '):
        return self.read_word(file).split(d)

    def read_ints(self, file, b=10, d=' '):
        return [int(x, b) for x in self.read_words(file, d)]

    def dot_product(self, v1, v2):
        dot_product = 0
        for i in range(len(v1)):
            dot_product += v1[i] * v2[i]
        return dot_product

    def solve(self):

        # create I/O files
        input_file = open(self.input_file_name, 'r')
        output_file = open(self.output_file_name, "w")

        # read file size
        T = self.read_int(input_file)

        # initialize cases to 1
        case = 1

        print("There are %d cases to solve! :)\n\n" % T)

        # iterate on each case
        for l in range(T):

            # get problem data
            dim = self.read_int(input_file)
            v1 = self.read_ints(input_file)
            v2 = self.read_ints(input_file)

            v1.sort()
            v2.sort()

            v2 = v2[::-1]

            prod = self.dot_product(v1,v2)

            output_file.write("Case #%d: %d\n" % (case,prod))
            case += 1

        # close I/O files
        input_file.close()
        output_file.close()


class Test(unittest.TestCase):

    def setUp(self):
        self.minimal_scalar_product = MinimumScalarProduct()

    def test_dot_product(self):
        self.assertEqual(self.minimal_scalar_product.dot_product([1],[1]),1)
        self.assertEqual(self.minimal_scalar_product.dot_product([1],[2]),2)
        self.assertEqual(self.minimal_scalar_product.dot_product([-1],[2]),-2)
        self.assertEqual(self.minimal_scalar_product.dot_product([-1],[-2]),2)
        self.assertEqual(self.minimal_scalar_product.dot_product([-1,3],[-2,-2]),-4)
        self.assertEqual(self.minimal_scalar_product.dot_product([1,3,-5],[-2,4,1]),5)

    def test_solve(self):
        # rw_sample = MinimumScalarProduct("B-sample.in", "B-sample.out")
        # rw_sample = MinimumScalarProduct("A-small-practice.in", "A-small-practice.out")
        rw_sample = MinimumScalarProduct("A-large-practice.in", "A-large-practice.out")
        rw_sample.solve()


if __name__ == '__main__':
    unittest.main()
