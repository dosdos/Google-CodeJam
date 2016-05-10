"""
Created on 30/04/2016

@author: Dos

Problem B. Close Match
https://code.google.com/codejam/contest/11254486/dashboard#s=p1


***Sample***

Input
4
1? 2?
?2? ??3
? ?
?5 ?0


Output
Case #1: 19 20
Case #2: 023 023
Case #3: 0 0
Case #4: 05 00

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
    w1 = kwargs['w1']
    w2 = kwargs['w2']
    r1 = ''
    r2 = ''
    c = 0

    int_found = False
    for i in xrange(len(w1)):
        if w1[i] == '?':
            if w2[i] != '?':
                r1 += w2[i]
                int_found = True
            else:
                if not int_found:
                    r1 += '0'
                else:
                    r1 += '0' if i > 0 and w1[i-1] > w2[i-1] else '9'
        else:
            r1 += w1[i]
            int_found = True

    int_found = False
    for i in xrange(len(w1)):
        if w2[i] == '?':
            if w1[i] != '?':
                r2 += w1[i]
                int_found = True
            else:
                if not int_found:
                    r2 += '0'
                else:
                    r2 += '0' if i > 0 and w1[i-1] < w2[i-1] else '9'
        else:
            r2 += w2[i]
            int_found = True

        c += 1

    return "Case #{}: {} {}\n".format(case, r1, r2)


# INPUT_FILE_NAME = "B-sample.in"
INPUT_FILE_NAME = "B-small-attempt3.in"
# INPUT_FILE_NAME = "B-large.in"

# OUTPUT_FILE_NAME = "B-sample.out"
OUTPUT_FILE_NAME = "B-small-attempt0.out"
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
        w1 = line_1[0]
        w2 = line_1[1]
        args = {'w1': w1, 'w2': w2, }

        print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        print(out)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
