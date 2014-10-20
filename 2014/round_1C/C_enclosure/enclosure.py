"""
Created on 11/05/apr/2014

@author: dosdos

Problem C. Name
http://code.google.com/codejam/contest/3004486/dashboard#s=p2



***Sample***

Input
2
4 5 8
3 5 11

Output
Case #1: 6
Case #2: 8

"""
import unittest



class ProblemC(object):

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


    def method_name(self, n):
        return n*n

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
            print("\nCase #%d: " % (case+1) )

            # get problem data
            line = self.read_ints(input_file)
            N = line[0] # rows
            M = line[1] # cols
            K = line[2] # intersection points to be enclosed
            stones = 0
            log_file.write("%d %d %d" % (N, M, K))
            print("%d %d %d" % (N, M, K))

            # base case 1
            if N == 1 or N == 2 or M == 1 or M == 2:
                # print the minimum number of stones needed
                output_file.write("Case #%d: %d\n" % (case+1,K))
                print("Case #%d: %d\n" % (case+1,K))

            # base case 2
            elif K >= (N*M - 4):
                diff = N*M - K
                stones = (N-2)*2 + (M-2)*2 + (4-diff)
                # print the minimum number of stones needed
                output_file.write("Case #%d: %d\n" % (case+1,stones))
                print("Case #%d: %d\n" % (case+1,stones))

            # standard case
            else:

                grid = self.create_grid(N, M)
                print(grid)
                centers = self.generate_centers(N, M)
                print(centers)

                for c in centers:
                    print("new enter set: ",c)

                    grid = self.put_stone(grid, N, M, c) # return cleaned grid
                    inters = self.count_intersections(grid, N, M)
                    stones = self.count_stones(grid, N, M)
                    print("put center, c=",c," inters=",inters," stones=",stones)
                    self.print_grid(grid)
                    if inters == K:
                        # print the minimum number of stones needed
                        output_file.write("Case #%d: %d\n" % (case+1,self.count_stones(grid, N, M)))
                        print("Case #%d: %d\n" % (case+1,self.count_stones(grid, N, M)))
                        break

                    # north
                    grid = self.put_stone(grid, N, M, self.get_north(c)) # the intersection in the north of the center
                    inters = self.count_intersections(grid, N, M)
                    stones = self.count_stones(grid, N, M)
                    print("put center, c=",c," inters=",inters," stones=",stones)
                    self.print_grid(grid)
                    if inters == K:
                        # print the minimum number of stones needed
                        output_file.write("Case #%d: %d\n" % (case+1,self.count_stones(grid, N, M)))
                        print("Case #%d: %d\n" % (case+1,self.count_stones(grid, N, M)))
                        break

                    # east
                    grid = self.put_stone(grid, N, M, self.get_east(c)) # the intersection in the east of the center
                    inters = self.count_intersections(grid, N, M)
                    stones = self.count_stones(grid, N, M)
                    print("put center, c=",c," inters=",inters," stones=",stones)
                    self.print_grid(grid)
                    if inters == K:
                        # print the minimum number of stones needed
                        output_file.write("Case #%d: %d\n" % (case+1,self.count_stones(grid, N, M)))
                        print("Case #%d: %d\n" % (case+1,self.count_stones(grid, N, M)))
                        break

                    # south
                    grid = self.put_stone(grid, N, M, self.get_south(c)) # the intersection in the south of the center
                    inters = self.count_intersections(grid, N, M)
                    stones = self.count_stones(grid, N, M)
                    print("put center, c=",c," inters=",inters," stones=",stones)
                    self.print_grid(grid)
                    if inters == K:
                        # print the minimum number of stones needed
                        output_file.write("Case #%d: %d\n" % (case+1,self.count_stones(grid, N, M)))
                        print("Case #%d: %d\n" % (case+1,self.count_stones(grid, N, M)))
                        break

                    # west
                    grid = self.put_stone(grid, N, M, self.get_west(c)) # the intersection in the west of the center
                    inters = self.count_intersections(grid, N, M)
                    stones = self.count_stones(grid, N, M)
                    print("put center, c=",c," inters=",inters," stones=",stones)
                    self.print_grid(grid)
                    if inters == K:
                        # print the minimum number of stones needed
                        output_file.write("Case #%d: %d\n" % (case+1,self.count_stones(grid, N, M)))
                        print("Case #%d: %d\n" % (case+1,self.count_stones(grid, N, M)))
                        break


        # close I/O files
        input_file.close()
        output_file.close()
        log_file.close()

    def create_grid(self, N, M):
        grid = []
        for i in range(N):
            row = []
            for j in range(M):
                row.append(2)
            grid.append(row)
        return grid

    def generate_centers(self, N, M):
        centers = [ (x+1,y+1) for x in range(N-2) for y in range(M-2) ]
        centers.sort(key=lambda c: c[0]+c[1])
        return centers

    def get_north(self, c):
        return (c[0]-1, c[1])

    def get_east(self, c):
        return (c[0], c[1]+1)

    def get_south(self, c):
        return (c[0]+1, c[1])

    def get_west(self, c):
        return (c[0], c[1]-1)

    def count_intersections(self, grid, N, M):
        inters = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0 or grid[i][j] == 1:
                    inters += 1
        return inters

    def count_stones(self, grid, N, M):
        stones = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    stones += 1
        return stones

    def put_stone(self, grid, N, M, c):
        if grid[c[0]][c[1]] != 1:
            grid[c[0]][c[1]] = 1
            grid = self.clean_grid(grid, N, M)
        return grid

    def clean_grid(self, grid, N, M):


        for i in range(N):
            for j in range(M):

                # check if there are stones on each edge
                if grid[i][j] == 1 and \
                            j >= 1 and grid[i][j-1] != 2 and \
                            i < N-1 and grid[i+1][j] != 2 and \
                            j < M-1 and grid[i][j+1] != 2 and \
                            i >= 1 and grid[i-1][j] != 2:

                    grid[i][j] = 0

        return grid

    def print_grid(self, grid):
        for row in grid:
            print(row)
        print("")


class Test(unittest.TestCase):
    def setUp(self):
        self.problem_C = ProblemC()

    def test_method(self):
        self.assertEqual(self.problem_C.method_name(1),1)

    def test_solve_small(self):
        # problem_C = ProblemC("C-sample.in", "C-sample.out", "C-log.out")
        problem_C = ProblemC("C-small-practice.in", "C-small-practice.out", "C-log.out")
        # problem_C = ProblemC("C-large-practice.in", "C-large-practice.out", "C-log.out")
        problem_C.solve_small()


if __name__ == '__main__':
    unittest.main()
