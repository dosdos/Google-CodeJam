"""
Created on 10/05/2015

@author: Dos

Problem A.
https://code.google.com/codejam/contest/4244486/dashboard


***Sample***

Input
3
1 4 2
1 7 7
2 5 1


Output
Case #1: 3
Case #2: 7
Case #3: 10

"""
from math import log


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
    R = kwargs['R']
    C = kwargs['C']
    W = kwargs['W']

    best = W

    if W == C:
        best = W
    else:
        guess1 = C / W
        guess2 = W - 1 if C % W == 0 else W

        print "guess 1: ", guess1
        print "guess 2: ", guess2
        best = (guess1 + guess2) * R

    return "Case #{}: {}\n".format(case, best)


# INPUT_FILE_NAME = "A-sample.in"
# INPUT_FILE_NAME = "A-small-attempt3.in"
INPUT_FILE_NAME = "A-large.in"

# OUTPUT_FILE_NAME = "A-sample.out"
# OUTPUT_FILE_NAME = "A-small-attempt3.out"
OUTPUT_FILE_NAME = "A-large.out"

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
        line_1 = read_ints(input_file)
        w1 = line_1[0]
        w2 = line_1[1]
        w3 = line_1[2]
        args = {'R': w1, 'C': w2, 'W': w3}

        print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        print(out)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
