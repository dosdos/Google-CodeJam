"""
Created on 08/04/2017

@author: Dos

Problem C.
https://code.google.com/codejam/contest/3264486/dashboard#s=p2


***Sample***

Input
5
4 2
5 2
6 2
1000 1000
1000 1

Output
Case #1: 1 0
Case #2: 1 0
Case #3: 1 1
Case #4: 0 0
Case #5: 500 499

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
    K = kwargs['K']
    l = r = 0

    acc = [N]

    if N / K < 2:
        return "Case #{}: 0 0\n"

    # print "acc", acc
    for _ in range(K):
        # m = acc.pop()
        m = max(acc)
        acc.remove(m)
        m -= 1
        l = m / 2 + (m % 2)
        r = m / 2
        if l:
            acc.append(l)
        if r:
            acc.append(r)
        # acc = sorted(acc)
        # print "acc", acc, l, r

    return "Case #{}: {} {}\n".format(case, max(l, r), min(l, r))


# INPUT_FILE_NAME = "C-sample.in"
# INPUT_FILE_NAME = "C-small-1-attempt2.in"
INPUT_FILE_NAME = "C-small-2-attempt0.in"
# INPUT_FILE_NAME = "C-large.in"

# OUTPUT_FILE_NAME = "C-sample.out"
# OUTPUT_FILE_NAME = "C-small-1-attempt2-bis.out"
OUTPUT_FILE_NAME = "C-small-2-attempt0.out"
# OUTPUT_FILE_NAME = "C-large.out"

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
        args = {'N': w1, 'K': w2}

        print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        print(out)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
