"""
Created on 05/apr/2014

@author: david

Problem A. Reverse Words
(https://code.google.com/codejam/contest/351101/dashboard#s=p1)


***Problem***

Given a list of space separated words, reverse the order of the words.
Each line of text contains L letters and W words. A line will only consist of letters and space characters.
There will be exactly one space character between each pair of consecutive words.

***Input***

The first line of input gives the number of cases, N.
N test cases follow. For each test case there will a line of letters and space characters indicating
a list of space separated words.
Spaces will not appear at the start or end of a line.

***Output***

For each test case, output one line containing "Case #x: " followed by the list of words in reverse order.

***Limits***

**Small dataset**

N = 5
1 ≤ L ≤ 25

**Large dataset**

N = 100
1 ≤ L ≤ 1000

***Sample***

Input
3
this is a test
foobar
all your base

Output
Case #1: test a is this
Case #2: foobar
Case #3: base your all


"""
__author__ = 'david'

import unittest


class ReverseWords(object):

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
            words = self.read_words(input_file)

            output_file.write("Case #%d: %s\n" % (case,' '.join(words[::-1])))

            case += 1

        # close I/O files
        input_file.close()
        output_file.close()


class Test(unittest.TestCase):

    def test_solve(self):
        # rw_sample = ReverseWords("B-sample.in", "B-sample.out")
        # rw_sample = ReverseWords("B-small-practice.in", "B-small-practice.out")
        rw_sample = ReverseWords("B-large-practice.in", "B-large-practice.out")
        rw_sample.solve()


if __name__ == '__main__':
    unittest.main()
