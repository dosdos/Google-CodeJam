"""
Created on 10/04/apr/2015

@author: Dos

Problem A. Consonants
https://code.google.com/codejam/contest/2437488/dashboard#s=p0


***Sample***

Input
3
3 aa
01 11 10
2 asd
101 111
2 dsa
01 10


Output
Case #1: 42
Case #2: 11
Case #3: 11

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
    N = kwargs['N']
    P = kwargs['P']
    L = kwargs['L']

    return "Case #{}: {}\n".format(case, L)


INPUT_FILE_NAME = "sample.in"
# INPUT_FILE_NAME = "A-small-attempt0.in"
# INPUT_FILE_NAME = "A-large.in"

OUTPUT_FILE_NAME = "sample.out"
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
    for case in range(T):
        # read input args
        line_1 = read_words(input_file)
        w1 = int(line_1[0])
        w2 = line_1[1]
        line_2 = read_ints(input_file)
        args = {'N': w1, 'P': w2, 'L': line_2}

        print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
