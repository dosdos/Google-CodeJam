"""
Created on 19/04/2015

@author: dosdos

Problem B. Haircut
https://code.google.com/codejam/contest/4224486/dashboard#s=p1


***Sample***

Input
3
2 4
10 5
3 12
7 7 7
3 8
4 2 1


Output
Case #1: 1
Case #2: 3
Case #3: 1

"""


def gcd(n, m):
    while m:
        n, m = m, n % m
    return n


def lcm_couple(n, m):
    return n * m // gcd(n, m)


def lcm(*args):
    return reduce(lcm_couple, args)


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
        line = read_ints(input_file)
        B = line[0]  # the number of barbers
        N = line[1]  # place in line
        minutes = read_ints(input_file)
        print("Input #%d:\n%d %d %s" % (case+1, B, N, str(minutes)))

        N = N % (lcm(*minutes) * B)
        print N

        barber = 1
        barbers = [0 for i in range(B)]
        remainings = N

        # print "barbers:", barbers, " - remainings=", remainings
        while remainings > 0:

            for i in range(B):
                if barbers[i] == 0:
                    barbers[i] = minutes[i]

                    if remainings > 0:
                        remainings -= 1

                    if remainings == 0:
                        barber = i + 1
                        break

            for i in range(B):
                barbers[i] -= 1

            # print "barbers:", barbers, " - remainings=", remainings

        # print output data!
        print("Case #%d: %s\n" % (case+1, barber))
        output_file.write("Case #%d: %d\n" % (case+1, barber))

    # close I/O files
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    # input_file_name = "B-sample.in"
    input_file_name = "B-small-practice.in"
    # input_file_name = "B-large-practice.in"

    # output_file_name = "B-sample.out"
    output_file_name = "B-small-practice.out"
    # output_file_name = "B-large-practice.out"

    solve(input_file_name, output_file_name)
