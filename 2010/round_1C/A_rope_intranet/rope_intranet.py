"""
Created on 09/apr/2014

@author: david

Problem A. Rope Intranet
(https://code.google.com/codejam/contest/32016/dashboard#s=p0)


***Problem***

A company is located in two very tall buildings. The company intranet connecting the buildings
consists of many wires, each connecting a window on the first building to a window on the second building.

You are looking at those buildings from the side, so that one of the buildings is to the left
and one is to the right. The windows on the left building are seen as points on its right wall,
and the windows on the right building are seen as points on its left wall. Wires are straight
segments connecting a window on the left building to a window on the right building.

You've noticed that no two wires share an endpoint (in other words, there's at most one wire going
out of each window). However, from your viewpoint, some of the wires intersect midway.
You've also noticed that exactly two wires meet at each intersection point.

On the above picture, the intersection points are the black circles, while the windows are the
white circles.

How many intersection points do you see?

***Input***

The first line of the input gives the number of test cases, T.
T test cases follow. Each case begins with a line containing an integer N, denoting the number
of wires you see.

The next N lines each describe one wire with two integers Ai and Bi.
These describe the windows that this wire connects: Ai is the height of the window on the left
building, and Bi is the height of the window on the right building.

***Output***

For each test case, output one line containing "Case #x: y", where x is the case number
(starting from 1) and y is the number of intersection points you see.

***Limits***

1 ≤ T ≤ 15.
1 ≤ Ai ≤ 104.
1 ≤ Bi ≤ 104.
Within each test case, all Ai are different.
Within each test case, all Bi are different.
No three wires intersect at the same point.

**Small dataset**

1 ≤ N ≤ 2.

**Large dataset**

1 ≤ N ≤ 1000.

***Sample***

Input
2
3
1 10
5 5
7 7
2
1 1
2 2

Output
Case #1: 2
Case #2: 0


"""
__author__ = 'david'

import unittest


class RopeIntranet(object):

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
        self.minimal_scalar_product = RopeIntranet()

    def test_dot_product(self):
        self.assertEqual(self.minimal_scalar_product.dot_product([1],[1]),1)
        self.assertEqual(self.minimal_scalar_product.dot_product([1],[2]),2)
        self.assertEqual(self.minimal_scalar_product.dot_product([-1],[2]),-2)
        self.assertEqual(self.minimal_scalar_product.dot_product([-1],[-2]),2)
        self.assertEqual(self.minimal_scalar_product.dot_product([-1,3],[-2,-2]),-4)
        self.assertEqual(self.minimal_scalar_product.dot_product([1,3,-5],[-2,4,1]),5)

    def test_solve(self):
        # ri_sample = RopeIntranet("B-sample.in", "B-sample.out")
        # ri_sample = RopeIntranet("A-small-practice.in", "A-small-practice.out")
        ri_sample = RopeIntranet("A-large-practice.in", "A-large-practice.out")
        ri_sample.solve()


if __name__ == '__main__':
    unittest.main()
