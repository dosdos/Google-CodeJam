"""
Created on 02/05/2015

@author: Dos

Problem B.
https://code.google.com/codejam/contest/


***Sample***

Input
WRITE_INTPUT_HERE

Output
WRITE_OUTPUT_HERE

"""
import unittest



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

            log_file.write("\nCase #%d: " % (case+1) )
            print("\nCase #%d: " % (case+1) )

            # get problem data
            N = self.read_int(input_file)
            line = self.read_ints(input_file)
            X = line[0]
            Y = line[1]
            counter = 0
            log_file.write("%d %s" % (N, line))
            print("%d %s" % (N, line))


            # print output data!
            output_file.write("Case #%d: %d\n" % (case+1,counter))

        # close I/O files
        input_file.close()
        output_file.close()
        log_file.close()


class Test(unittest.TestCase):
    def setUp(self):
        self.problem_B = ProblemB()

    def test_method(self):
        self.assertEqual(self.problem_B.method_name(1),1)

    def test_solve_small(self):
        problem_B = ProblemB("B-sample.in", "B-sample.out", "B-log.out")
        # problem_B = ProblemB("B-small-attempt0.in", "B-small-attempt0.out", "B-log.out")
        # problem_B = ProblemB("B-large-attempt0.in", "B-large-attempt0.out", "B-log.out")
        problem_B.solve_small()


if __name__ == '__main__':
    unittest.main()
