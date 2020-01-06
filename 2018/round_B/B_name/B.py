"""
Created on 22/04/2017

@author: Dos

Problem B.
https://code.google.com/codejam/contest/8294486/dashboard#s=p1


***Sample***

Input
4
6 2 0 2 0 2 0
3 1 0 2 0 0 0
6 2 0 1 1 2 0
4 0 0 2 0 0 2

Output
Case #1: RYBRBY
Case #2: IMPOSSIBLE
Case #3: YBRGRB
Case #4: YVYV

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
    N = kwargs['N']
    colors = kwargs['ints']
    labels = ['R', 'O', 'Y', 'G', 'B', 'V']
    neib = {
        'R': ['Y', 'G', 'B'],
        'O': ['B'],
        'Y': ['B', 'V', 'R'],
        'G': ['R'],
        'B': ['Y', 'R', 'O'],
        'V': ['Y'],
    }
    ponies = {}
    for i, color in enumerate(colors):
        if color:
            ponies[labels[i]] = color

    prev = max(ponies, key=ponies.get)
    ponies[prev] -= 1
    if ponies[prev] == 0:
        ponies.pop(prev)
    res = prev
    print res

    while ponies:
        prev_neib = {c: ponies[c] for c in neib[prev] if c in ponies}
        if not prev_neib:
            break

        if 'O' in prev_neib.keys():
            m = 'O'
        elif 'G' in prev_neib.keys():
            m = 'G'
        elif 'V' in prev_neib.keys():
            m = 'V'
        else:
            m = max(ponies, key=prev_neib.get)
        ponies[m] -= 1
        if ponies[m] == 0:
            ponies.pop(m)
        res += m
        prev = m
        print res, m

    if len(res) != N or res[-1] not in neib[res[0]]:
        return "Case #{}: {}\n".format(case, "IMPOSSIBLE")
    else:
        return "Case #{}: {}\n".format(case, res)


INPUT_FILE_NAME = "B-sample.in"
# INPUT_FILE_NAME = "B-small-attempt0.in"
# INPUT_FILE_NAME = "B-large.in"

OUTPUT_FILE_NAME = "B-sample.out"
# OUTPUT_FILE_NAME = "B-small-attempt0.out"
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
        line_1 = read_ints(input_file)
        args = {'N': line_1[0], 'ints': line_1[1:]}

        print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        print(out)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
