"""
Created on 26/apr/2014

@author: dosdos

Problem A. Charging Chaos
https://code.google.com/codejam/contest/2984486/dashboard#s=p0



***Sample***

Input
3
3 2
01 11 10
11 00 10
2 3
101 111
010 001
2 2
01 10
10 01

Output
Case #1: 1
Case #2: NOT POSSIBLE
Case #3: 0

"""
import unittest
import itertools


class ChargingChaos(object):

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


    def flip(self, l, i):
        """ Flip the i-th bit for each element of l, where l is a list of 01-array of the same length.
        """
        l2 = []
        for elem in l:
            sl = list(elem)
            sl[i] = '0' if sl[i] == '1' else '1'
            l2.append(''.join(sl))
        return l2

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

            log_file.write("\nCase #%d: \n" % (case+1) )

            # get problem data
            line = self.read_ints(input_file)
            N = line[0] # number of 01 strings
            L = line[1] # string length
            # 'initial' and 'required' are N space-separated strings of length L
            initial = self.read_words(input_file)
            required = self.read_words(input_file)

            # initial.sort()
            required.sort()

            log_file.write("%s %s %s %s" % (N, L, initial, required))

            # calculate all combinations of index to flip (there are L indexes)
            to_flip = range(L)
            flip_subsets = []
            for L in range(0, len(to_flip)+1):
                for subset in itertools.combinations(to_flip, L):
                    flip_subsets.append(subset)

            # for each possible combinations, do the flip and check if the new list matches with required
            for to_s in flip_subsets:
                new_initial = initial
                for s in to_s:
                    print(new_initial,s)
                    new_initial = self.flip(new_initial,s)
                new_initial.sort()
                if new_initial == required:
                    print(len(to_s))
                    output_file.write("Case #%d: %d\n" % (case+1,len(to_s)))
                    break
            else:
                print("NOT POSSIBLE")
                output_file.write("Case #%d: %s\n" % (case+1,"NOT POSSIBLE"))


        # close I/O files
        input_file.close()
        output_file.close()
        log_file.close()


    def solve_large(self):
        # create I/O files
        input_file = open(self.input_file_name, 'r')
        output_file = open(self.output_file_name, "w")
        log_file = open(self.log_file_name, "w")

        # read file size
        T = self.read_int(input_file)

        log_file.write("There are %d cases to solve! :)\n" % T)

        # iterate on each case
        for case in range(T):

            log_file.write("\nCase #%d: \n" % (case+1) )

            # get problem data
            line = self.read_ints(input_file)
            N = line[0] # number of 01 strings
            L = line[1] # string length
            # 'initial' and 'required' are N space-separated strings of length L
            initial = self.read_words(input_file)
            required = self.read_words(input_file)

            # initial.sort()
            required.sort()

            log_file.write("%s %s %s %s" % (N, L, initial, required))

            # itero sugli initial i
            # provo a collegare il device 0 all'outlet i flippando i suoi bit di conseguenza

            # registro i bit che ho flippato e provo la combinazione su tutti i device

            # se la combinazione matcha mi fermo



            # calculate all combinations of index to flip (there are L indexes)
            to_flip = range(L)
            flip_subsets = []
            for L in range(0, len(to_flip)+1):
                for subset in itertools.combinations(to_flip, L):
                    flip_subsets.append(subset)

            # for each possible combinations, do the flip and check if the new list matches with required
            for to_s in flip_subsets:
                new_initial = initial
                for s in to_s:
                    print(new_initial,s)
                    new_initial = self.flip(new_initial,s)
                new_initial.sort()
                if new_initial == required:
                    print(len(to_s))
                    output_file.write("Case #%d: %d\n" % (case+1,len(to_s)))
                    break
            else:
                print("NOT POSSIBLE")
                output_file.write("Case #%d: %s\n" % (case+1,"NOT POSSIBLE"))


        # close I/O files
        input_file.close()
        output_file.close()
        log_file.close()


class Test(unittest.TestCase):
    def setUp(self):
        self.problem_A = ChargingChaos()

    def test_flip(self):
        self.assertEqual(self.problem_A.flip(['101'],1),['111'])
        self.assertEqual(self.problem_A.flip(['01', '10', '11'],0),['11', '00', '01'])
        self.assertEqual(self.problem_A.flip(['101', '111'],0),['001', '011'])

    def test_solve_small(self):
        pass
        # problem_A = ChargingChaos("A-sample.in", "A-sample.out", "A-log.out")
        # problem_A = ChargingChaos("A-small-attempt0.in", "A-small-attempt0.out", "A-log.out")
        # problem_A = ChargingChaos("A-small-practice.in", "A-small-practice.out", "A-log.out")
        # problem_A.solve_small()

    def test_solve_large(self):
        problem_A = ChargingChaos("A-sample.in", "A-sample.out", "A-log.out")
        # problem_A = ChargingChaos("A-large-attempt0.in", "A-large-attempt0.out", "A-log.out")
        problem_A.solve_large()


if __name__ == '__main__':
    unittest.main()
