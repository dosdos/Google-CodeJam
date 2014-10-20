"""
Created on 12/apr/2014

@author: dosdos

Problem C. Minesweeper Master
(https://code.google.com/codejam/contest/2974486/dashboard#s=p2)

***Limits***

0 ≤ M < R * C.

***Small dataset***

1 ≤ T ≤ 230.
1 ≤ R, C ≤ 5.

***Large dataset***

1 ≤ T ≤ 140.
1 ≤ R, C ≤ 50.


***Sample***

Input
5
5 5 23
3 1 1
2 2 1
4 7 3
10 10 82

Output
Case #1:
Impossible
Case #2:
c
.
*
Case #3:
Impossible
Case #4:
......*
.c....*
.......
..*....
Case #5:
**********
**********
**********
****....**
***.....**
***.c...**
***....***
**********
**********
**********




"""
import re

__author__ = 'david'

import unittest


class MinesweeperMaster(object):

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

    def read_decimal(self, file, b=10, d=' '):
        return [float(x) for x in self.read_words(file, d)]

    def get_max_mines(self, r, c):
        if r == 1 or c ==1:
            min_mines = r*c - 2
        else:
            min_mines = r*c - 4
        return min_mines

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
            data = self.read_ints(input_file)
            rows = data[0] # rows
            cols = data[1] # cols
            mines = data[2] # mines

            print("Case #%d:\t" % (case),"%dx%d" % (rows,cols), "\t", mines)

            output_file.write("Case #%d:\n" % (case))
            if mines <= self.get_max_mines(rows,cols):
                counter = 1
                for r in range(rows):
                    line = ""
                    for c in range(cols):
                        if r == rows-1 and c == cols-1:
                            line += "c"
                        elif counter <= mines and not ( (r == rows-2 and c == cols-1) or (r == rows-2 and c == cols-2) ):
                            line += "*"
                            counter += 1
                        else:
                            line += "."
                    output_file.write(line+"\n")
            else:
                output_file.write("Impossible\n")
            case += 1

        # close I/O files
        input_file.close()
        output_file.close()


class Test(unittest.TestCase):
    def setUp(self):
        self.minesweeper_master = MinesweeperMaster()

    def test_max_mines(self):
        self.assertEqual(self.minesweeper_master.get_max_mines(5,5),21)
        self.assertEqual(self.minesweeper_master.get_max_mines(10,10),96)
        self.assertEqual(self.minesweeper_master.get_max_mines(4,7),24)
        self.assertEqual(self.minesweeper_master.get_max_mines(3,1),1)
        self.assertEqual(self.minesweeper_master.get_max_mines(2,2),0)

    def test_solve(self):
        # mm_sample = MinesweeperMaster("C-sample.in", "C-sample.out")
        mm_sample = MinesweeperMaster("C-small-attempt0.in", "C-small-attempt0.out")
        # mm_sample = MinesweeperMaster("C-large.in", "C-large.out")
        mm_sample.solve()


if __name__ == '__main__':
    unittest.main()
