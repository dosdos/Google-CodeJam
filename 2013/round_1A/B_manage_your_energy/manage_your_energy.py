"""
Created on 21/apr/2014

@author: dosdos

Problem B. Manage your Energy
(https://code.google.com/codejam/contest/2418487/dashboard#s=p1)

***Limits***

1 ≤ T ≤ 100.

***Small dataset***

1 ≤ E ≤ 5.
1 ≤ R ≤ 5.
1 ≤ N ≤ 10.
1 ≤ vi ≤ 10.

***Large dataset***

1 ≤ E ≤ 107.
1 ≤ R ≤ 107.
1 ≤ N ≤ 104.
1 ≤ vi ≤ 107.


***Sample***

Input
3
5 2 2
2 1
5 2 2
1 2
3 3 4
4 1 3 5

Output
Case #1: 12
Case #2: 12
Case #3: 39


"""
import unittest


class ManageYourEnergy(object):

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


    def solve(self):

        # create I/O files
        input_file = open(self.input_file_name, 'r')
        output_file = open(self.output_file_name, "w")

        # read file size
        T = self.read_int(input_file)

        # initialize cases to 1
        case = 1
        cps = 2.0 # cookie per seconds

        print("There are %d cases to solve! :)\n\n" % T)

        # iterate on each case
        for l in range(T):

            # get problem data
            data = self.read_decimal(input_file)
            C = data[0] # cost per farm
            F = data[1] # cookie frequency per farm
            X = data[2] # goal cookies

            freq = cps
            found = False
            farms = 1. # current number of farms
            total_to_buy_farms = 0. # seconds spent to buy farms
            prev_seconds = X / cps

            while not found:
                to_buy_farm = C / freq
                freq = cps + farms*F # update frequency
                to_reach_goal = X / freq
                total_to_buy_farms += to_buy_farm

                if (total_to_buy_farms + to_reach_goal) > prev_seconds:
                    found = True
                    break

                prev_seconds = total_to_buy_farms + to_reach_goal
                farms +=1

            # write output file
            output_file.write("Case #%d: %s\n" % (case,str(prev_seconds)))
            case += 1

        # close I/O files
        input_file.close()
        output_file.close()


class Test(unittest.TestCase):

    def test_solve(self):
        mye_sample = ManageYourEnergy("B-sample.in", "B-sample.out")
        # mye_sample = ManageYourEnergy("B-small-practice.in", "B-small-practice.out")
        # mye_sample = ManageYourEnergy("B-large-practice.in", "B-large-practice.out")
        mye_sample.solve()


if __name__ == '__main__':
    unittest.main()
