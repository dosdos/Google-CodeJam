"""
Created on 23/apr/2014

@author: dosdos

Problem A. Bullseye
https://code.google.com/codejam/contest/2434486/dashboard



***Sample***

Input
4
2 2
2 1
2 4
2 1 1 6
10 4
25 20 9 100
1 4
1 1 1 1

Output
Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 4

"""
import unittest



class Osmos(object):

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


    def get_extra_motes(self, A, mote):
        extra_motes = []
        while mote-A >= 0:
            extra_motes.append(A-1)
            A += A-1
        return extra_motes


    def solve_small(self):

        # create I/O files
        input_file = open(self.input_file_name, 'r')
        output_file = open(self.output_file_name, "w")

        # read file size
        T = self.read_int(input_file)

        # initialize cases to 1
        case = 1


        for t in range(T):
            print('Case #%d:' % (t+1))

            # get problem data
            line = self.read_ints(input_file)
            my_mote = line[0] # the size of Armin's mote
            n = line[1] # the number of other motes
            motes = self.read_ints(input_file)
            motes.sort()


            if my_mote == 1:
                print (n)

            best_answer = n
            my_answer = 0

            for index, i in enumerate(motes):
                if i < my_mote:
                    my_mote += i
                    continue
                # maybe stop here?
                best_answer = min([best_answer, my_answer + n - index])
                while my_mote <= i:
                    my_mote += my_mote - 1
                    my_answer += 1
                my_mote += i
            best_answer = min([best_answer, my_answer])
            print(best_answer)


        # close I/O files
        input_file.close()
        output_file.close()


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

            print("\nCase #%d: " % case)

            # get problem data
            line = self.read_ints(input_file)
            A = line[0] # the size of Armin's mote
            N = line[1] # the number of other motes
            motes = self.read_ints(input_file)
            print(A, N, motes)
            ops = 0 # the minimum number of operations needed to make the game solvable.
            motes.sort()

            print("Armin:", A, " - motes", motes, " - operations", ops,)

            while len(motes)>0:

                # limit case: Armin mote is not not enough to start playing
                if A <= 1:
                    ops += len(motes)
                    motes = []
                    print("Armin:", A, " - motes", motes, " - operations", ops,)
                    break
                # limit case: operations needed are more than N
                # if ops >= N-1:
                #     ops = N
                #     motes = []
                #     print("Armin:", A, " - motes", motes, " - operations", ops,)
                #     break
                # base case: Armin mote is big enough
                elif motes[0]<A:
                    m = motes.pop(0)
                    A += m
                # recursive case: Armin mote is not big enough
                else:
                    extra_motes = self.get_extra_motes(A, motes[0])
                    if len(motes) < ( len(extra_motes) + ops ):
                        ops += len(motes)
                        motes = []
                        print("Armin:", A, " - motes", motes, " - operations", ops,)
                        break
                    else:
                        # motes = extra_motes + motes
                        ops += len(extra_motes)
                        print("extra motes added", extra_motes)
                        for em in extra_motes:
                            A += em

                print("Armin:", A, " - motes", motes, " - operations", ops,)

            output_file.write("Case #%d: %d\n" % (case,ops))
            case += 1

        # close I/O files
        input_file.close()
        output_file.close()


class Test(unittest.TestCase):
    def setUp(self):
        self.osmos = Osmos()

    def test_get_extra_motes(self):
        self.assertEqual(self.osmos.get_extra_motes(11,19),[10])
        self.assertEqual(self.osmos.get_extra_motes(11,30),[10,20])
        self.assertEqual(self.osmos.get_extra_motes(8,50),[7,14,28])
        self.assertEqual(self.osmos.get_extra_motes(6,6),[5])
        # self.assertEqual(self.osmos.get_extra_motes(1,1),[])

    def test_solve_small(self):
        # o = Osmos("B-sample.in", "B-sample.out")
        o = Osmos("A-small-practice.in", "A-small-practice.out")
        # o = Osmos("A-large-practice.in", "A-large-practice.out")
        o.solve_small()


if __name__ == '__main__':
    unittest.main()
