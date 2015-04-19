"""
Created on 11/04/apr/2015

@author: dosdos

Problem C. Dijkstra
https://code.google.com/codejam/contest/6224486/dashboard#s=p2


***Sample***

Input
5
2 1
ik
3 1
ijk
3 1
kji
2 6
ji
1 10000
i


Output
Case #1: NO
Case #2: YES
Case #3: NO
Case #4: YES
Case #5: NO

"""


def read_word(f):
    return next(f).strip()


def read_int(f, b=10):
    return int(read_word(f), b)


def read_words(f, d=' '):
    return read_word(f).split(d)


def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]


q = {
    ("1", "1"): "1",
    ("1", "i"): "i",
    ("1", "j"): "j",
    ("1", "k"): "k",

    ("i", "1"): "i",
    ("i", "i"): "-1",
    ("i", "j"): "k",
    ("i", "k"): "-j",

    ("j", "1"): "j",
    ("j", "i"): "-k",
    ("j", "j"): "-1",
    ("j", "k"): "i",

    ("k", "1"): "k",
    ("k", "i"): "j",
    ("k", "j"): "-i",
    ("k", "k"): "-1",
}


def multiply(a, b):
    prefix = ""
    if a[0] == "-":
        prefix = "-"
    if b[0] == "-":
        prefix = "" if prefix == "-" else "-"
    res = q[(a[-1], b[-1])]
    if res[0] == "-":
        prefix = "" if prefix == "-" else "-"
    return prefix + q[(a[-1], b[-1])][-1]


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
        line = read_ints(input_file)
        L = line[0]
        X = line[1]
        s = read_word(input_file)
        print("Input #%d:\n%d %d %s" % (case+1, L, X, s))

        y = "YES"
        n = "NO"
        can_reduce = n
        found_i = False
        found_j = False
        found_k = False
        part = "1"

        # print curr

        for i in range(L*X):
            curr = s[i%L]
            # print "curr=", curr, "index=", i
            # print part, "*", curr, "=", multiply(part, curr)
            part = multiply(part, curr)

            if not found_i and (part == "i" or part == "1" and curr == "i"):
                found_i = True
                part = "1"
                # print "FOUND i! :)"
                continue
            elif found_i and not found_j and (part == "j" or part == "1" and curr == "j"):
                found_j = True
                part = "1"
                # print "FOUND j! :)"
                continue
            elif found_i and found_j and not found_k and (part == "k" or part == "1" and curr == "k"):
                found_k = True
                part = "1"
                # print "FOUND k! :)"
                continue

        if found_i and found_j and found_k and part == "1":
            can_reduce = y

        # print output data!
        print("Case #%d: %s\n" % (case+1, can_reduce))
        output_file.write("Case #%d: %s\n" % (case+1, can_reduce))

    # close I/O files
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    input_file_name = "C-sample.in"
    # input_file_name = "C-small-attempt0.in"
    # input_file_name = "C-large.in"

    output_file_name = "C-sample.out"
    # output_file_name = "C-small-attempt0.out"
    # output_file_name = "C-large.out"

    solve(input_file_name, output_file_name)

    # print multiply("j", "i")
