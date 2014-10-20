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

    rows = 1
    cols = 1
    mines = 0
    grid = []

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

    def set_grid(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.mines = rows*cols
        self.grid = [ ['*' for i in range(cols)] for j in range(rows)]

    def print_grid(self):
        for i in range(self.rows):
            print(self.grid[i])

    def fill_row(self, mines):

        if self.rows == 1 and mines <= self.cols-2:
            for c in range(mines,self.cols-1):
                self.grid[0][c] = '.'
            self.grid[0][self.cols-1] = 'c'
            return True
        else:
            return False

    def fill_col(self, mines):
        if self.cols == 1 and mines <= self.rows-2:
            for r in range(mines,self.rows-1):
                self.grid[r][0] = '.'
            self.grid[self.rows-1][0] = 'c'
            return True
        else:
            return False

    def click(self, r, c):
        if self.grid[r][c] != '.':
            self.grid[r][c] = '.'
            self.mines -= 1

        # N
        if r-1 >= 0 and self.grid[r-1][c] != '.':
            self.grid[r-1][c] = '.'
            self.mines -= 1

        # NE
        if r-1 >= 0 and c+1 < self.cols and self.grid[r-1][c+1] != '.':
            self.grid[r-1][c+1] = '.'
            self.mines -= 1

        # E
        if c+1 < self.cols and self.grid[r][c+1] != '.':
            self.grid[r][c+1] = '.'
            self.mines -= 1

        # SE
        if r+1 < self.rows and c+1 < self.cols and self.grid[r+1][c+1] != '.':
            self.grid[r+1][c+1] = '.'
            self.mines -= 1

        # S
        if r+1 < self.rows and self.grid[r+1][c] != '.':
            self.grid[r+1][c] = '.'
            self.mines -= 1

        # SO
        if r+1 < self.rows and c-1 >= 0 and self.grid[r+1][c-1] != '.':
            self.grid[r+1][c-1] = '.'
            self.mines -= 1

        # O
        if c-1 >= 0 and self.grid[r][c-1] != '.':
            self.grid[r][c-1] = '.'
            self.mines -= 1

        # NO
        if r-1 >=0 and c-1 >= 0 and self.grid[r-1][c-1] != '.':
            self.grid[r-1][c-1] = '.'
            self.mines -= 1


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
            master = MinesweeperMaster()
            master.set_grid(rows,cols)

            if rows == 1: # 1-row case

                if master.fill_row(mines):
                    for i in range(master.cols):
                        output_file.write(master.grid[0][i])
                    output_file.write("\n")
                else:
                    output_file.write("Impossible\n")

            elif cols == 1: # 1-column case

                if master.fill_col(mines):
                    for r in master.grid:
                        output_file.write(r[0])
                        output_file.write("\n")
                else:
                    output_file.write("Impossible\n")

            elif mines > rows*cols - 4: # rectangular case with too many mines

                output_file.write("Impossible\n")

            else: # rectangular case

                click_r = 0
                click_c = 0
                master.click(click_r, click_c)

                while master.mines >= mines:
                    master.print_grid()
                    print("Mines:", mines, " - master.mines:", master.mines, "\n")

                    if master.mines == mines:
                        for r in range(rows):
                            for c in range(cols):
                                output_file.write(master.grid[r][c])
                            output_file.write("\n")
                        break

                    if click_r < rows-1:
                        click_r += 1
                    else:
                        click_r = 0
                        click_c += 1

                    master.click(click_r, click_c)

                else:
                    output_file.write("Impossible\n")


            case += 1

        # close I/O files
        input_file.close()
        output_file.close()



class Test(unittest.TestCase):
    def setUp(self):
        self.minesweeper_master = MinesweeperMaster()

    def testPrintGrid(self):
        print("\ntestPrintGrid starting ...")
        grid = MinesweeperMaster()
        grid.set_grid(5,5)
        grid.print_grid()
        grid.set_grid(3,3)
        grid.print_grid()
        grid.set_grid(2,4)
        grid.print_grid()
        grid.set_grid(5,1)
        grid.print_grid()
        grid.set_grid(1,5)
        grid.print_grid()
        grid.set_grid(1,1)
        grid.print_grid()

    def testClick(self):
        print("\ntestClick starting ...")
        master = MinesweeperMaster()
        master.set_grid(3,3)
        master.click(2,2) # count rows and cols starting from 0
        target_grid = [ ['*', '*', '*'] , ['*', '.', '.'] , ['*', '.', '.'] ]
        self.assertEqual(master.grid,target_grid)
        self.assertEqual(master.mines,5)
        master.print_grid()

        master.click(0,2) # count rows and cols starting from 0
        target_grid = [ ['*', '.', '.'] , ['*', '.', '.'] , ['*', '.', '.'] ]
        self.assertEqual(master.grid,target_grid)
        self.assertEqual(master.mines,3)
        master.print_grid()

    def testRowGrid(self):
        print("\ntestRowGrid starting ...")
        master = MinesweeperMaster()
        master.set_grid(1,5)
        self.assertTrue(master.fill_row(2))
        self.assertEqual(master.grid,[['*', '*', '.', '.', 'c']])
        master.set_grid(1,1)
        self.assertFalse(master.fill_row(2))
        master.set_grid(1,2)
        self.assertFalse(master.fill_row(2))
        master.set_grid(1,3)
        self.assertFalse(master.fill_row(2))
        master.set_grid(1,6)
        self.assertTrue(master.fill_row(3))
        self.assertEqual(master.grid,[['*', '*', '*', '.', '.', 'c']])

    def testColGrid(self):
        print("\ntestColGrid starting ...")
        master = MinesweeperMaster()
        master.set_grid(5,1)
        self.assertTrue(master.fill_col(2))
        self.assertEqual(master.grid,[['*'], ['*'], ['.'], ['.'], ['c']])
        master.set_grid(1,1)
        self.assertFalse(master.fill_col(2))
        master.set_grid(2,1)
        self.assertFalse(master.fill_col(2))
        master.set_grid(3,1)
        self.assertFalse(master.fill_col(2))
        master.set_grid(6,1)
        self.assertTrue(master.fill_col(3))
        self.assertEqual(master.grid,[['*'], ['*'], ['*'], ['.'], ['.'], ['c']])

    def test_solve(self):
        # mm_sample = MinesweeperMaster("C-sample.in", "C-sample.out")
        mm_sample = MinesweeperMaster("C-small-attempt3.in", "C-small-attempt3.out")
        # mm_sample = MinesweeperMaster("C-large.in", "C-large.out")
        mm_sample.solve()


if __name__ == '__main__':
    unittest.main()
