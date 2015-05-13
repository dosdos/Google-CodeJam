"""
Created on 10/05/2015

@author: Dos

Problem B.
https://code.google.com/codejam/contest/4244486/dashboard


***Sample***

Input
5
7 6 6
BANANAS
MONKEY
2 3 4
AA
AAA
2 1 2
AB
B
6 2 2
GOOGLE
GO
26 11 100
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ROSENCRANTZ

Output
Case #1: 0.0
Case #2: 0.0
Case #3: 1.0
Case #4: 0.8888889
Case #5: 9.0

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


def find_prefix(s):
    p = ""
    for i in range(len(s)):
        if s[:i] == s[-i:]:
            p = s[:i]

    return len(p)


print find_prefix("gogogd")


def solve(case, **kwargs):
    # get problem data
    K = kwargs['K']
    L = kwargs['L']
    S = kwargs['S']
    keyword = kwargs['keyword']
    target = kwargs['target']

    result = -1
    is_possible = True

    clean_keyword = {}
    for c in keyword:
        if c in clean_keyword:
            clean_keyword[c] += 1
        else:
            clean_keyword[c] = 1

    for c in target:
        if c not in clean_keyword:
            is_possible = False
            break

    if is_possible:
        prob = 1
        for c in target[find_prefix(target):]:

            print c, clean_keyword[c] * (1. / K)
            prob *= clean_keyword[c] * (1. / K)

        print "prob=", prob

    else:
        result = 0.0

    return "Case #{}: {}\n".format(case, result)


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
        line_2 = read_word(input_file)
        line_3 = read_word(input_file)
        args = {'K': w1, 'L': w2, 'S': w3, 'keyword': line_2, 'target': line_3}

        print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        print(out)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
