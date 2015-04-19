"""
Created on 11/04/apr/2015

@author: dosdos

Problem A. Ominus Omino
https://code.google.com/codejam/contest/6224486/dashboard#s=p3


***Sample***

Input
4
2 2 2
2 1 3
4 4 1
3 2 3


Output
Case #1: GABRIEL
Case #2: RICHARD
Case #3: RICHARD
Case #4: GABRIEL

"""


def read_word(f):
    return next(f).strip()


def read_int(f, b=10):
    return int(read_word(f), b)


def read_words(f, d=' '):
    return read_word(f).split(d)


def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]


def solve(file_in, file_out):
    # create I/O files
    input_file = open(file_in, 'r')
    output_file = open(file_out, "w")

    # read file size
    T = read_int(input_file)
    gab = "GABRIEL"
    ric = "RICHARD"
    winner = gab

    print("There are %d cases to solve! :)\n" % T)

    # iterate on each case
    for case in range(T):

        # get problem data
        line = read_ints(input_file)
        X = line[0]  # number of tiles of X-omino
        R = line[1]  # grid rows
        C = line[2]  # grid cols
        print("Input #%d:\n%d %d %d" % (case+1, X, R, C))

        if X == 1:
            winner = gab

        elif X == 2:
            if R*C % 2 == 0:
                winner = gab
            else:
                winner = ric

        elif X == 3:
            if (R == 3 or C == 3) and not (R == 1 or C == 1):
                winner = gab
            else:
                winner = ric

        elif X == 4:
            if (R == 4 and C == 3) or (R == 3 and C == 4) or (R == 4 and C == 4):
                winner = gab
            else:
                winner = ric

        # print output data!
        print("Case #%d: %s\n" % (case+1, winner))
        output_file.write("Case #%d: %s\n" % (case+1, winner))

    # close I/O files
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    # input_file_name = "D-sample.in"
    input_file_name = "D-small-attempt0.in"
    # input_file_name = "D-large.in"

    # output_file_name = "D-sample.out"
    output_file_name = "D-small-attempt0.out"
    # output_file_name = "D-large.out"

    solve(input_file_name, output_file_name)
