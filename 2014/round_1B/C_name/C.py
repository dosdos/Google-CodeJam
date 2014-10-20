"""
Created on 26/apr/2014

@author: dosdos

Problem C. The Bored Traveling Salesman
https://code.google.com/codejam/contest/2994486/dashboard#s=p2



***Sample***

Input
4
3 2
10001
20000
10000
1 2
2 3
5 4
36642
28444
50012
29651
10953
1 4
2 3
2 5
4 5
5 5
36642
28444
50012
29651
10953
1 2
1 4
2 3
2 5
4 5
6 6
10001
10002
10003
10004
10005
10006
1 2
1 6
2 3
2 4
3 5
4 5

Output
Case #1: 100002000010001
Case #2: 1095328444500122965136642
Case #3: 1095328444366422965150012
Case #4: 100011000210003100041000510006

"""
import unittest



class TheBoredTravelingSalesman(object):

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

    def read_decimals(self, file, b=10, d=' '):
        return [float(x) for x in self.read_words(file, d)]


    def get_neighbours(self, node, graph):
        neighbours = []
        for n in graph:
            if n[0] == node:
                neighbours.append(n[1])
            elif n[1] == node:
                neighbours.append(n[0])
        return neighbours


    def solve_small(self):

        # create I/O files
        input_file = open(self.input_file_name, 'r')
        output_file = open(self.output_file_name, "w")
        log_file = open(self.log_file_name, "w")

        # read file size
        T = self.read_int(input_file)

        log_file.write("There are %d cases to solve! :)\n" % T)
        print("There are %d cases to solve! :)\n" % T)

        # iterate on each case
        for case in range(T):

            log_file.write("\nCase #%d: " % (case+1) )

            # get problem data
            data = self.read_ints(input_file)
            N = data[0] # the number of cities
            M = data[1] # the number of possible bidirectional flights

            start_zips = []
            for i in range(N):
                start_zips.append(self.read_int(input_file))

            print(start_zips)

            flights = []
            for i in range(M):
                city_flight = self.read_ints(input_file)
                flights.append((city_flight[0],city_flight[1]))

            print(flights)

            log_file.write("%d %s" % (N, M, ))

            zips = start_zips
            path = []
            current = zips.pop(zips.index(min(zips)))
            path.append(current)

            for i in range(N-1):
                neighbours = self.get_neighbours(start_zips.index(current),start_zips)
                neighbours_zips = []

                for n in neighbours:
                    neighbours_zips.append(start_zips[n])
                next = min(neighbours_zips)
                city = zips.index(next)
                zips.pop(city)
                current = city

            print('z',zips, current)

            output_file.write("Case #%d: %s\n" % (case+1,"BAD"))

        # close I/O files
        input_file.close()
        output_file.close()
        log_file.close()



class Test(unittest.TestCase):
    def setUp(self):
        self.problem_C = TheBoredTravelingSalesman()

    def test_get_neighbours(self):
        self.assertEqual( self.problem_C.get_neighbours(2,[(1,2),(2,3),(3,4)]) , [1,3] )

    def test_solve_small(self):
        problem_C = TheBoredTravelingSalesman("C-sample.in", "C-sample.out", "C-log.out")
        # problem_C = TheBoredTravelingSalesman("C-small-attempt0.in", "C-small-attempt0.out", "C-log.out")
        # problem_C = TheBoredTravelingSalesman("C-large-attempt0.in", "C-large-attempt0.out", "C-log.out")
        problem_C.solve_small()


if __name__ == '__main__':
    unittest.main()
