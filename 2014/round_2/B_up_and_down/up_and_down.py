"""
Created on 12/04/2015

@author: dosdos

Problem A. Up and Down
https://code.google.com/codejam/contest/3014486/dashboard#s=p1



***Sample***

Input
2
3
1 2 3
5
1 8 10 3 7

Output
Case #1: 0
Case #2: 1

"""
import unittest
from math import log


class ProblemB(object):

    def __init__(self, input_file_name=None, output_file_name=None, log_file_name=None):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.log_file_name = log_file_name

    # file I/O
    def read_word(self, file):
        return next(file).strip()

    def read_int(self, file, b=10):
        return int(self.read_word(file), b)

    def read_words(self, file, d=' '):
        return self.read_word(file).split(d)

    def read_ints(self, file, b=10, d=' '):
        return [int(x, b) for x in self.read_words(file, d)]

    def read_decimals(self, file, b=10, d=' '):
        return [float(x) for x in self.read_words(file, d)]

    def method_name(self, n):
        return n*n

    def solve_small(self):

        # create I/O files
        input_file = open(self.input_file_name, 'r')
        output_file = open(self.output_file_name, "w")
        log_file = open(self.log_file_name, "w")

        # read file size
        T = self.read_int(input_file)

        log_file.write("There are %d cases to solve! :)\n" % T)
        print("There are %d cases to solve! :)\n" % T)

        # iterate on each case
        for case in range(T):

            # get problem data
            N = self.read_int(input_file)
            samples = self.read_ints(input_file)

            swap = 0
            sx = 0
            dx = len(samples) - 1

            while sx < dx:
                min_idx = samples.index(min(samples[sx:dx+1]))

                # print "i:", min_idx, " sx:", sx, " dx:", dx, "samples[sx:dx]:", samples[sx:dx], " \n"

                if min_idx == sx:
                    sx += 1
                elif min_idx == dx:
                    dx -= 1
                elif min_idx - sx >= dx - min_idx:
                    samples[min_idx], samples[min_idx+1] = samples[min_idx+1], samples[min_idx]
                    swap += 1
                    if min_idx == dx-1:
                        dx -= 1
                elif min_idx - sx < dx - min_idx:
                    samples[min_idx], samples[min_idx-1] = samples[min_idx-1], samples[min_idx]
                    swap += 1
                    if min_idx == sx+1:
                        sx += 1

            # print output data!
            print("Case #%d: %d\n" % (case+1, swap))
            output_file.write("Case #%d: %d\n" % (case+1, swap))

        # close I/O files
        input_file.close()
        output_file.close()
        log_file.close()


class Test(unittest.TestCase):
    def setUp(self):
        self.problem_B = ProblemB()

    def test_method(self):
        self.assertEqual(self.problem_B.method_name(1), 1)

    def test_solve_small(self):
        # problem_B = ProblemB("B-sample.in", "B-sample.out", "B-log.out")
        # problem_B = ProblemB("B-small-practice.in", "B-small-practice.out", "B-log.out")
        problem_B = ProblemB("B-large-practice.in", "B-large-practice.out", "B-log.out")
        problem_B.solve_small()


if __name__ == '__main__':
    unittest.main()
