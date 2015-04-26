"""
Created on 02/05/2015

@author: Dos

Problem A. Password Problem
https://code.google.com/codejam/contest/1645485/dashboard#s=p0


***Sample***

Input
3
2 5
0.6 0.6
1 20
1
3 4
1 0.9 0.1

Output
Case #1: 7.000000
Case #2: 20.000000
Case #3: 4.500000

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


def solve(case, **kwargs):
    # get problem data
    A = kwargs['A']
    B = kwargs['B']
    p = kwargs['p_list']

    best, x = B + 2.0, 1
    for i in xrange(A):
        x *= p[i]
        best = min(best, (B - i) + (A - i - 1) + (B + 1) * (1 - x))

    return "Case #%d: %.6f\n" % (case, best)


INPUT_FILE_NAME = "A-sample.in"
# INPUT_FILE_NAME = "A-small-practice.in"
# INPUT_FILE_NAME = "A-large-practice.in"

OUTPUT_FILE_NAME = "A-sample.out"
# OUTPUT_FILE_NAME = "A-small-practice.out"
# OUTPUT_FILE_NAME = "A-large-practice.out"

if __name__ == '__main__':

    # create I/O files
    input_file = open(INPUT_FILE_NAME, 'r')
    output_file = open(OUTPUT_FILE_NAME, "w")

    # read file size
    T = read_int(input_file)
    print("\nThere are %d cases to solve! :)\n" % T)

    # iterate on each case
    for case in range(1, T+1):
        # read input args
        line_1 = read_ints(input_file)
        line_2 = read_decimals(input_file)
        args = {'A': line_1[0], 'B': line_1[1], 'p_list': line_2}

        print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        print(out)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
