"""
Created on 10/04/apr/2015

@author: dosdos

Problem A. Mushroom Monster
https://code.google.com/codejam/contest/4224486/dashboard#s=p0


***Sample***

Input
4
4
10 5 15 5
2
100 100
8
81 81 81 81 81 81 81 0
6
23 90 40 0 100 9


Output
Case #1: 4
Case #2: 11
Case #3: 3
Case #4: 11

"""


def read_word(f):
    return next(f).strip()


def read_int(f, b=10):
    return int(read_word(f), b)


def read_words(f, d=' '):
    return read_word(f).split(d)


def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]


def read_decimals(f, d=' '):
    return [float(x) for x in read_words(f, d)]


def solve(file_in, file_out):
    # create I/O files
    input_file = open(file_in, 'r')
    output_file = open(file_out, "w")

    # read file size
    T = read_int(input_file)

    print("\nThere are %d cases to solve! :)\n" % T)

    # iterate on each case
    for case in range(T):

        # get problem data
        N = read_int(input_file)
        dishes = read_ints(input_file)
        print("Input #%d:\n%d %s" % (case+1, N, str(dishes)))

        c1 = 0
        c2 = 0

        prev = dishes[0]
        for i in range(1, N):
            diff = dishes[i]-prev
            if diff < 0:
                c1 += abs(diff)
            prev = dishes[i]

        max_diff = 0
        for i in range(N-1):
            diff = dishes[i]-dishes[i+1]
            if diff > max_diff:
                max_diff = diff

        for i in range(N-1):
            print(dishes[i])
            if dishes[i] < max_diff:
                c2 += dishes[i]
            else:
                c2 += max_diff

        # print output data!
        print("Case #%d: %d %d\n" % (case+1, c1, c2))
        output_file.write("Case #%d: %d %d\n" % (case+1, c1, c2))

    # close I/O files
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    input_file_name = "A-sample.in"
    # input_file_name = "A-small-practice.in"
    # input_file_name = "A-large-practice.in"

    output_file_name = "A-sample.out"
    # output_file_name = "A-small-practice.out"
    # output_file_name = "A-large-practice.out"

    solve(input_file_name, output_file_name)
