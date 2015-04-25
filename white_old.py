"""
Created on 10/04/apr/2015

@author: Dos

Problem A. Consonants
https://code.google.com/codejam/contest/2437488/dashboard#s=p0


***Sample***

Input
3
3 aa
01 11 10
2 asd
101 111
2 dsa
01 10


Output
Case #1: 42
Case #2: 11
Case #3: 11

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
        w1 = int(line[0])
        w2 = line[1]
        nums = read_ints(input_file)
        print("%d %s %s" % (w1, w2, str(nums)))
        print("Input #%d:\n%d %s %s" % (case+1, w1, w2, str(nums)))

        counter = 0

        # print output data!
        print("Case #%d: %s\n" % (case+1, counter))
        output_file.write("Case #%d: %d\n" % (case+1, counter))

    # close I/O files
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    input_file_name = "sample.in"
    # input_file_name = "A-small-attempt0.in"
    # input_file_name = "A-large.in"

    output_file_name = "sample.out"
    # output_file_name = "A-small-attempt0.out"
    # output_file_name = "A-large.out"

    solve(input_file_name, output_file_name)
