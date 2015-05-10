"""
Created on 02/05/2015

@author: Dos

Problem A.
https://code.google.com/codejam/contest/


***Sample***

Input
3
1
19
23

Output
Case #1: 1
Case #2: 19
Case #3: 15

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


def rev(n):
    return int(str(n)[::-1])


def solve(case, **kwargs):
    # get problem data
    N = kwargs['N']


    for i in range(1, N+1):

        print rev(i)


    return "Case #{}: {}\n".format(case, N)


INPUT_FILE_NAME = "A-sample.in"
# INPUT_FILE_NAME = "A-small-attempt0.in"
# INPUT_FILE_NAME = "A-large.in"

OUTPUT_FILE_NAME = "A-sample.out"
# OUTPUT_FILE_NAME = "A-small-attempt0.out"
# OUTPUT_FILE_NAME = "A-large.out"

if __name__ == '__main__':

    # create I/O files
    input_file = open(INPUT_FILE_NAME, 'r')
    output_file = open(OUTPUT_FILE_NAME, "w")

    # read file size
    T = read_int(input_file)
    print("\nThere are %d cases to solve! :)\n" % T)

    # iterate on each case
    for case in xrange(1, T+1):
        # read input args
        w1 = read_int(input_file)
        args = {'N': w1}

        print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        print(out)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
