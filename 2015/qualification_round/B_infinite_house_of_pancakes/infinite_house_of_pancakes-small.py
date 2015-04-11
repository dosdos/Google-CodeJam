"""
Created on 11/04/apr/2015

@author: dosdos

Problem A. Standing Ovation
https://code.google.com/codejam/contest/6224486/dashboard#s=p0


***Sample***

Input
3
1
3
4
1 2 1 2
1
4


Output
Case #1: 3
Case #2: 2
Case #3: 3

"""


def read_word(f):
    return next(f).strip()


def read_int(f, b=10):
    return int(read_word(f), b)


def read_words(f, d=' '):
    return read_word(f).split(d)


def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]


def split_pancakes(pancakes):

    if len(pancakes) == 1 and pancakes[0] == 9:
        return [6, 3]

    if len(pancakes) >= 2 and pancakes[0] == 9:
        if pancakes[1] <= 3 or pancakes[1] == 6:
            pancakes.append(6)
            pancakes.append(3)
            return sorted(pancakes[1:], reverse=True)

    pancakes.append(pancakes[0] / 2 + pancakes[0] % 2)
    pancakes.append(pancakes[0] / 2)
    return sorted(pancakes[1:], reverse=True)


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
        D = read_int(input_file)
        pancakes = read_ints(input_file)
        print("Input #%d:\n%d %s" % (case+1, D, str(pancakes)))

        best = max(pancakes)
        special = 0
        pancakes = sorted(pancakes, reverse=True)

        while pancakes[0] > 3:
            pancakes = split_pancakes(pancakes)
            special += 1
            if pancakes[0] + special < best:
                best = pancakes[0] + special

        # print output data!
        print("Case #%d: %s\n" % (case+1, best))
        output_file.write("Case #%d: %d\n" % (case+1, best))

    # close I/O files
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    # input_file_name = "B-sample.in"
    input_file_name = "B-small-attempt3.in"
    # input_file_name = "B-large.in"

    # output_file_name = "B-sample.out"
    output_file_name = "B-small-attempt3.out"
    # output_file_name = "B-large.out"

    solve(input_file_name, output_file_name)

    # print split_pancakes([9, 4, 3])
