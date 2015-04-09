"""
Created on 10/04/apr/2015

@author: dosdos

Problem A. Consonants
https://code.google.com/codejam/contest/2437488/dashboard#s=p0


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

    print("There are %d cases to solve! :)\n" % T)

    # iterate on each case
    for case in range(T):
        print("\nCase #%d: " % (case + 1))

        # get problem data
        line = read_words(input_file)
        N = int(line[0])
        nums = line[1:]
        print("%d %s" % (N, str(nums)))

        counter = 0
        print("Case #%d: %s\n" % (case, 1))

        # print output data!
        output_file.write("Case #%d: %d\n" % (case + 1, counter))

    # close I/O files
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    input_file_name = "A-sample.in"
    output_file_name = "A-sample.out"
    solve(input_file_name, output_file_name)
