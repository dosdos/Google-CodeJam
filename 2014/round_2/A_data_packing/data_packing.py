"""
Created on 12/04/2015

@author: dosdos

Problem A. Data Packing
https://code.google.com/codejam/contest/3014486/dashboard#s=p0



***Sample***

Input
3
3 100
10 20 70
4 100
30 40 60 70
5 100
10 20 30 40 60

Output
Case #1: 2
Case #2: 2
Case #3: 3

"""
import unittest
from math import log


class ProblemA(object):

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
            line = self.read_ints(input_file)
            N = line[0]  # the number of files to be stored
            X = line[1]  # the capacity of the discs to be used
            files = self.read_ints(input_file)

            # Sort files
            files = sorted(files)

            i = 0
            j = len(files) - 1
            c = 0
            while i <= j:
                if files[i] + files[j] <= X:
                    i += 1
                j -= 1
                c += 1

            # print output data!
            print("Case #%d: %d\n" % (case+1, c))
            output_file.write("Case #%d: %d\n" % (case+1, c))

        # close I/O files
        input_file.close()
        output_file.close()
        log_file.close()


class Test(unittest.TestCase):
    def setUp(self):
        self.problem_A = ProblemA()

    def test_method(self):
        self.assertEqual(self.problem_A.method_name(1), 1)

    def test_solve_small(self):
        # problem_A = ProblemA("A-sample.in", "A-sample.out", "A-log.out")
        # problem_A = ProblemA("A-small-practice.in", "A-small-practice.out", "A-log.out")
        problem_A = ProblemA("A-large-practice.in", "A-large-practice.out", "A-log.out")
        problem_A.solve_small()


if __name__ == '__main__':
    unittest.main()
