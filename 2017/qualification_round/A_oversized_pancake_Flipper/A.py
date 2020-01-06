"""
Created on 08/04/2017

@author: Dos

Problem A.
https://code.google.com/codejam/contest/3264486/dashboard#s=p0


***Sample***

Input
3
---+-++- 3
+++++ 4
-+-+- 4

Output
Case #1: 3
Case #2: 0
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
    S = kwargs['S']
    K = kwargs['K']

    counter = 0

    l = list(S)
    for i in xrange(len(l) - K + 1):
        p = l[i]
        print "-----", i, p, l
        if p == '-':
            for k in range(i, i+K):
                if l[k] == '-':
                    l[k] = '+'
                else:
                    l[k] = '-'
            counter += 1
            print '+1', counter

    print "FINAL: ", l
    if '-' in l:
        return "Case #{}: IMPOSSIBLE\n".format(case)
    else:
        return "Case #{}: {}\n".format(case, counter)


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
        line_1 = read_words(input_file)
        w1 = line_1[0]
        w2 = int(line_1[1])
        args = {'S': w1, 'K': w2}

        print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        print(out)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
