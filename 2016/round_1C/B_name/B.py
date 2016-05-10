"""
Created on 08/05/2016

@author: Dos

Problem B. Slides!
https://code.google.com/codejam/contest/4314486/dashboard#s=p1


***Sample***

Input
3
5 4
2 1
4 20

Output
Case #1: POSSIBLE
01001
00110
00001
00101
00000
Case #2: POSSIBLE
01
00
Case #3: IMPOSSIBLE

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
    B = kwargs['B']
    M = kwargs['M']

    res = ''
    if M > (2**(B-2)):
        res += "IMPOSSIBLE\n"
    else:
        res += "POSSIBLE\n"

        for i in xrange(B):
            for j in xrange(B):
                res += '0'
            res += '\n'

    return "Case #{}: {}".format(case, res)


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
        args = {'B': w1, 'M': w2, }

        print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        print(out)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
