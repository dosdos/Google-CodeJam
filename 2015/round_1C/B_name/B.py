"""
Created on 10/05/2015

@author: Dos

Problem B.
https://code.google.com/codejam/contest/4244486/dashboard


***Sample***

Input
WRITE_INTPUT_HERE

Output
WRITE_OUTPUT_HERE

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


INPUT_FILE_NAME = "B-sample.in"
# INPUT_FILE_NAME = "B-small-attempt0.in"
# INPUT_FILE_NAME = "B-large.in"

OUTPUT_FILE_NAME = "B-sample.out"
# OUTPUT_FILE_NAME = "B-small-attempt0.out"
# OUTPUT_FILE_NAME = "B-large.out"

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
        line_1 = read_words(input_file)
        w1 = int(line_1[0])
        w2 = line_1[1]
        line_2 = read_ints(input_file)
        args = {'N': w1, 'P': w2, 'L': line_2}

        print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        print(out)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
