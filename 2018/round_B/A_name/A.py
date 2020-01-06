"""
Created on 22/04/2017

@author: Dos

Problem A.
https://code.google.com/codejam/contest/8294486/dashboard


***Sample***

Input
3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10

Output
Case #1: 101.000000
Case #2: 100.000000
Case #3: 33.333333

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
    D = kwargs['D']
    horses = kwargs['horses']

    speeds = [(D-h[0])*1.0/h[1] for h in horses]
    result = D * 1. / max(speeds)

    return "Case #{}: {}\n".format(case, round(result, 6))


# INPUT_FILE_NAME = "A-sample.in"
# INPUT_FILE_NAME = "A-small-attempt1.in"
INPUT_FILE_NAME = "A-large.in"

# OUTPUT_FILE_NAME = "A-sample.out"
# OUTPUT_FILE_NAME = "A-small-attempt1.out"
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
        w1 = int(line_1[0])
        w2 = int(line_1[1])
        horses = []
        for i in xrange(w2):
            line_2 = read_ints(input_file)
            horses.append([int(line_2[0]), int(line_2[1])])
        args = {'D': w1, 'horses': horses}

        print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        print(out)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
