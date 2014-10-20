"""
Created on 26/apr/2014

@author: dosdos

Problem B. Full Binary Tree
https://code.google.com/codejam/contest/2984486/dashboard#s=p1



***Sample***

Input
3
3
2 1
1 3
7
4 5
4 2
1 2
3 1
6 4
3 7
4
1 2
2 3
3 4

Output
Case #1: 0
Case #2: 2
Case #3: 1

"""
import unittest



class FullBinaryTree(object):

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


    def method_name(self, A, mote):
        extra_motes = []
        while mote-A >= 0:
            extra_motes.append(A-1)
            A += A-1
        return extra_motes

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

            tree = []
            for i in range(N-1):
                line = self.read_ints(input_file)
                # Xi Yi, indicating that G contains an undirected edge between Xi and Yi.
                X = line[0]
                Y = line[1]
                tree.append((X,Y))

            # calcola il numero di foglie
            #

            print("%s %s" % (N, tree))

            counter = 0

            output_file.write("Case #%d: %d\n" % (case+1,counter))

        # close I/O files
        input_file.close()
        output_file.close()
        log_file.close()


class Test(unittest.TestCase):
    def setUp(self):
        self.problem_B = FullBinaryTree()

    def test_get_extra_motes(self):
        self.assertEqual(self.problem_B.method_name(11,19),[10])
        self.assertEqual(self.problem_B.method_name(11,30),[10,20])
        self.assertEqual(self.problem_B.method_name(8,50),[7,14,28])
        self.assertEqual(self.problem_B.method_name(6,6),[5])

    def test_solve_small(self):
        problem_B = FullBinaryTree("B-sample.in", "B-sample.out", "B-log.out")
        # problem_B = Name("B-small-attempt0.in", "B-small-attempt0.out", "B-log.out")
        # problem_B = Name("B-large-attempt0.in", "B-large-attempt0.out", "B-log.out")
        problem_B.solve_small()


if __name__ == '__main__':
    unittest.main()
