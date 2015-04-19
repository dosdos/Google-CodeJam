"""
Created on 11/04/apr/2015

@author: dosdos

Problem A. Standing Ovation
https://code.google.com/codejam/contest/6224486/dashboard#s=p0


***Sample***

Input
4
4 11111
1 09
5 110011
0 1


Output
Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 0

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

    print("There are %d cases to solve! :)\n" % T)

    # iterate on each case
    for case in range(T):

        # get problem data
        line = read_words(input_file)
        s_max = int(line[0])
        s = line[1]
        print("Input #%d:\n%d %s" % (case+1, s_max, s))

        invitees = 0
        clapping = 0

        for i in range(s_max+1):
            curr = int(s[i])

            if curr != 0 and clapping + invitees < i:
                invitees += i - (clapping + invitees)

            clapping += curr

        # print output data!
        print("Case #%d: %s\n" % (case+1, invitees))
        output_file.write("Case #%d: %d\n" % (case+1, invitees))

    # close I/O files
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    # input_file_name = "B-sample.in"
    # input_file_name = "A-small-attempt0.in"
    input_file_name = "A-large.in"

    # output_file_name = "A-sample.out"
    # output_file_name = "A-small-attempt0.out"
    output_file_name = "A-large.out"

    solve(input_file_name, output_file_name)
