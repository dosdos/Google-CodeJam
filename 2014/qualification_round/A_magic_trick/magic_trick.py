"""
Created on 12/apr/2014

@author: dosdos

Problem A. Magic Trick
(https://code.google.com/codejam/contest/2974486/dashboard#s=p0)

"""
import re

__author__ = 'david'

import unittest


class MagicTrick(object):

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


    def number_of_matching(self, a1, a2):
        n = 0 # the number of matches
        m = -1 # the last matching number
        for i in a1:
            if i in a2:
                n += 1
                m = i
        return n, m


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
            answer_1 = self.read_int(input_file)
            r1 = self.read_ints(input_file)
            r2 = self.read_ints(input_file)
            r3 = self.read_ints(input_file)
            r4 = self.read_ints(input_file)
            arrangement_1 = [r1,r2,r3,r4]
            print(arrangement_1)

            answer_2 = self.read_int(input_file)
            s1 = self.read_ints(input_file)
            s2 = self.read_ints(input_file)
            s3 = self.read_ints(input_file)
            s4 = self.read_ints(input_file)
            arrangement_2 = [s1,s2,s3,s4]
            print(arrangement_2)

            matched, last_matched = self.number_of_matching(arrangement_1[answer_1-1],arrangement_2[answer_2-1])

            if matched == 0:
                result = "Volunteer cheated!"
            elif matched == 1:
                result = str(last_matched)
            else:
                result = "Bad magician!"

            output_file.write("Case #%d: %s\n" % (case,result))
            case += 1

        # close I/O files
        input_file.close()
        output_file.close()


class Test(unittest.TestCase):
    def setUp(self):
        self.magic_trick = MagicTrick()

    def test_language_to_regex(self):
        self.assertEqual(self.magic_trick.number_of_matching([5,6,7,8],[9,10,7,12]), (1,7))
        self.assertEqual(self.magic_trick.number_of_matching([5,6,7,8],[5,6,7,8]), (4,8))
        self.assertEqual(self.magic_trick.number_of_matching([5,6,7,8],[9,10,11,12]), (0,-1))

    def test_solve(self):
        # mt_sample = MagicTrick("B-sample.in", "B-sample.out")
        mt_sample = MagicTrick("A-small-attempt0.in", "A-small-attempt0.out")
        # mt_sample = MagicTrick("A-large-practice.in", "A-large-practice.out")
        mt_sample.solve()


if __name__ == '__main__':
    unittest.main()
