"""
Created on 26/apr/2014

@author: dosdos

Problem C. Name
https://code.google.com/codejam/contest/2984486/dashboard#s=p2



***Sample***

Input
2
3
0 1 2
3
2 0 1

Output
Case #1: BAD
Case #2: GOOD

"""
import unittest



class ProperShuffle(object):

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


    def solve_small(self):

        # create I/O files
        input_file = open(self.input_file_name, 'r')
        output_file = open(self.output_file_name, "w")
        log_file = open(self.log_file_name, "w")

        # read file size
        T = self.read_int(input_file)

        log_file.write("There are %d cases to solve! :)\n" % T)

        # iterate on each case
        for case in range(T):

            log_file.write("\nCase #%d: " % (case+1) )

            # get problem data
            N = self.read_int(input_file)
            data = self.read_ints(input_file)
            log_file.write("%d %s" % (N, data))

            counter = 0


            output_file.write("Case #%d: %s\n" % (case+1,"BAD"))

        # close I/O files
        input_file.close()
        output_file.close()
        log_file.close()


class Test(unittest.TestCase):
    def setUp(self):
        self.problem_C = ProperShuffle()

    def test_solve_small(self):
        # problem_C = ProperShuffle("C-sample.in", "C-sample.out", "C-log.out")
        problem_C = ProperShuffle("C-small-practice.in", "C-small-practice.out", "C-log.out")
        # problem_C = ProperShuffle("C-large-attempt0.in", "C-large-attempt0.out", "C-log.out")
        problem_C.solve_small()


if __name__ == '__main__':
    unittest.main()
