"""
Created on 05/apr/2014

@author: david

Problem A. Store Credit
(https://code.google.com/codejam/contest/351101/dashboard#s=p0)


***Problem***

You receive a credit C at a local store and would like to buy two items.
You first walk through the store and create a list L of all available items.
From this list you would like to buy two items that add up to the entire value of the credit.
The solution you provide will consist of the two integers indicating the positions
of the items in your list (smaller number first).

***Input***

The first line of input gives the number of cases, N. N test cases follow. For each test case there will be:

 - One line containing the value C, the amount of credit you have at the store.
 - One line containing the value I, the number of items in the store.
 - One line containing a space separated list of I integers. Each integer P indicates the price of an item in the store.
 - Each test case will have exactly one solution.

***Output***

For each test case, output one line containing "Case #x: " followed by the indices of the
two items whose price adds up to the store credit. The lower index should be output first.

***Limits***

5 ≤ C ≤ 1000
1 ≤ P ≤ 1000

***Small dataset***

N = 10
3 ≤ I ≤ 100

***Large dataset***

N = 50
3 ≤ I ≤ 2000

***Sample***

Input
3
100
3
5 75 25
200
7
150 24 79 50 88 345 3
8
8
2 1 9 4 4 56 90 3

Output
Case #1: 2 3
Case #2: 1 4
Case #3: 4 5

"""
__author__ = 'david'

import unittest


class StoreCredit(object):

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
        for l in range(0,T):

            # get problem data
            credit = self.read_ints(input_file)[0]
            num_of_items = self.read_ints(input_file)[0]
            item_prices = self.read_ints(input_file)

            # print(str(credit), str(num_of_items), str(item_prices))

            found = False
            i = 0

            while not found and i < len(item_prices)-1:

                for j in range(i+1,len(item_prices)):
                    # print(item_prices[i],item_prices[j])
                    if item_prices[i] + item_prices[j] == credit:
                        print("ok! %d %d" % (i+1,j+1))
                        output_file.write("Case #%d: %d %d\n" % (case,i+1,j+1))
                        found = True
                i += 1

            case += 1

        # close I/O files
        input_file.close()
        output_file.close()


class Test(unittest.TestCase):

    def test_solve(self):
        # sc_sample = StoreCredit("B-sample.in", "B-sample.out")
        # sc_sample = StoreCredit("A-small-practice.in", "A-small-practice.out")
        sc_sample = StoreCredit("A-large-practice.in", "A-large-practice.out")
        sc_sample.solve()


if __name__ == '__main__':
    unittest.main()
