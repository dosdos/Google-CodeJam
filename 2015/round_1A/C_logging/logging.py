"""
Created on 10/04/apr/2015

@author: dosdos

Problem C. Logging
https://code.google.com/codejam/contest/4224486/dashboard#s=p2


***Sample***

Input
2
5
0 0
10 0
10 10
0 10
5 5
9
0 0
5 0
10 0
0 5
5 5
10 5
0 10
5 10
10 10


Output
Case #1:
0
0
0
0
1
Case #2:
0
0
0
0
3
0
0
0
0

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
    trees = kwargs['trees']

    return "Case #{}: {}\n".format(case, trees)


INPUT_FILE_NAME = "C-sample.in"
# INPUT_FILE_NAME = "C-small-attempt0.in"
# INPUT_FILE_NAME = "C-large.in"

OUTPUT_FILE_NAME = "C-sample.out"
# OUTPUT_FILE_NAME = "C-small-attempt0.out"
# OUTPUT_FILE_NAME = "C-large.out"

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
        N = read_int(input_file)
        l = []
        for i in range(N):
            point = read_ints(input_file)
            l.append((point[0], point[1]))
        args = {'N': N, 'trees': l}

        print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        print(out)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
