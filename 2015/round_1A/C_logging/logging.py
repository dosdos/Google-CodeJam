"""
Created on 10/04/apr/2015

@author: dosdos

Problem C. Logging
https://code.google.com/codejam/contest/4224486/dashboard#s=p2


***Sample***

Input
4
quartz 3
straight 3
gcj 2
tsetse 2


Output
Case #1: 4
Case #2: 11
Case #3: 3
Case #4: 11

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


def solve(file_in, file_out):
    # create I/O files
    input_file = open(file_in, 'r')
    output_file = open(file_out, "w")

    # read file size
    T = read_int(input_file)

    print("\nThere are %d cases to solve! :)\n" % T)

    # iterate on each case
    for case in range(T):

        # get problem data
        line = read_words(input_file)
        w1 = line[0]
        w2 = line[1]
        print("%d %s" % (w1, w2))
        print("Input #%d:\n%d %d" % (case+1, w1, w2))

        counter = 0

        # print output data!
        # print output data!
        print("Case #%d: %s\n" % (case+1, counter))
        output_file.write("Case #%d: %d\n" % (case+1, counter))

    # close I/O files
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    input_file_name = "reverse_long.txt"
    # input_file_name = "A-small-practice.in"
    # input_file_name = "A-large-practice.in"

    output_file_name = "out.txt"
    # output_file_name = "A-small-practice.out"
    # output_file_name = "A-large-practice.out"

    solve(input_file_name, output_file_name)
