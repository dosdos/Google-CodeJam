"""
Created on 02/05/2015

@author: Dos

Problem B.
https://code.google.com/codejam/contest/


***Sample***

Input
4
2 3 6
4 1 2
3 3 8
5 2 0

Output
Case #1: 7
Case #2: 0
Case #3: 8
Case #4: 0

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
    R = kwargs['R']
    C = kwargs['C']
    N = kwargs['N']

    if R > C:
        R, C = C, R

    if R==1 and C==1:
        max_ok = 1
        empty_angles = 0
        empty_edges = 0
        empty_center = 0
    elif R==1:
        max_ok = (R*C)/2 + (R*C)%2
        empty_angles = 1
        empty_edges = C/2 - empty_angles
        empty_center = 0
    else:
        max_ok = (R*C)/2 + (R*C)%2
        empty_angles = 0 if ((R*C)%2) else 2
        empty_edges = (R*2 + C*2 - 4) / 2 - empty_angles
        empty_center = R*C - max_ok - empty_angles - empty_edges

    print "max_ok:", max_ok,\
        "empty_angles:", empty_angles,\
        "empty_edges:", empty_edges,\
        "empty_center:", empty_center

    walls = 0
    to_add = N

    # fill optimal
    if N <= max_ok:
        walls = 0
        to_add = 0

    # fill angles
    if to_add > 0:
        walls += empty_angles * 2
        to_add -= empty_angles

    # fill edges
    if to_add > 0:
        walls += empty_edges * 3
        to_add -= empty_edges

    # fill center
    if to_add > 0:
        walls += empty_center * 4

    return "Case #{}: {}\n".format(case, walls)


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
        line_1 = read_ints(input_file)
        w1 = line_1[0]
        w2 = line_1[1]
        w3 = line_1[2]
        args = {'R': w1, 'C': w2, 'N': w3}

        print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        print(out)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
