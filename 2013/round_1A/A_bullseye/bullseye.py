"""
Created on 21/apr/2014

@author: dosdos

Problem A. Bullseye
(https://code.google.com/codejam/contest/2418487/dashboard#s=p0)

"""
import unittest
import math

PI = math.pi


class Bullseye(object):

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


    def ring_area_1(self, r, n):
        return (r+2*n-1) **2 - (r+2*n-2) **2

    def ring_area_2(self, r, n):
        return 2*r + 4*n - 3 # ring_area_1 simplified


    def solve_small(self):

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
            line = self.read_ints(input_file)
            r = line[0] # Maria draws the first black ring around a white circle of radius r cm
            t = line[1] # Maria starts with t millilitres of black paint
            rings = 0 # the maximum number of black rings that Maria can draw
            print(r,t)

            ring_area = self.ring_area_2(r,rings+1)
            print(ring_area)
            while ring_area <= t:
                rings += 1
                t -= ring_area
                ring_area = self.ring_area_2(r,rings+1)
                print(ring_area, ' t=', t)

            output_file.write("Case #%d: %d\n" % (case,rings))
            case += 1

        # close I/O files
        input_file.close()
        output_file.close()


    def solve_large(self):

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
            line = self.read_ints(input_file)
            r = line[0] # Maria draws the first black ring around a white circle of radius r cm
            t = line[1] # Maria starts with t millilitres of black paint
            rings = 0 # the maximum number of black rings that Maria can draw
            print(r,t)

            #### TODO ####

            output_file.write("Case #%d: %d\n" % (case,rings))
            case += 1

        # close I/O files
        input_file.close()
        output_file.close()

class Test(unittest.TestCase):
    def setUp(self):
        self.bullseye = Bullseye()

    def test_ring_area(self):
        self.assertEqual(self.bullseye.ring_area_1(1,9),self.bullseye.ring_area_2(1,9))
        self.assertEqual(self.bullseye.ring_area_1(1,10),self.bullseye.ring_area_2(1,10))
        self.assertEqual(self.bullseye.ring_area_1(3,40),self.bullseye.ring_area_2(3,40))
        # self.assertEqual(self.bullseye.ring_area_1(1,1000000000000000000),self.bullseye.ring_area_2(1,1000000000000000000))
        # self.assertEqual(self.bullseye.ring_area_1(10000000000000000,1000000000000000000),self.bullseye.ring_area_2(10000000000000000,1000000000000000000))

    def test_solve_small(self):
        # be = Bullseye("B-sample.in", "B-sample.out")
        be = Bullseye("A-small-practice.in", "A-small-practice.out")
        be.solve_small()

    def test_solve_large(self):
        pass
        # be = Bullseye("A-large-practice.in", "A-large-practice.out")
        # be.solve_large()


if __name__ == '__main__':
    unittest.main()
