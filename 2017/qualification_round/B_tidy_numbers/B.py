"""
Created on 08/04/2017

@author: Dos

Problem B.
https://code.google.com/codejam/contest/3264486/dashboard#s=p1


***Sample***

Input
4
132
1000
7
111111111111111110

Output
Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999

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
    num = list(N)
    sub = {
        '0': '9',
        '1': '0',
        '2': '1',
        '3': '2',
        '4': '3',
        '5': '4',
        '6': '5',
        '7': '6',
        '8': '7',
        '9': '8',
    }
    l = len(num)
    for i in xrange(l - 1, 0, -1):
        if int(num[i]) < int(num[i-1]):
            num[i] = '9'
            num[i-1] = sub[num[i-1]]

    num = ''.join(num)
    num = num.lstrip('0')
    nine = num.find('9')
    num = (num[:nine+1] + '9'*(l - nine - 1)) if nine >= 0 else num
    num = num[1:] if num[0] == '9' and N[0] != '9' else num
    return "Case #{}: {}\n".format(case, num)


# INPUT_FILE_NAME = "B-sample.in"
# INPUT_FILE_NAME = "B-small-attempt1.in"
INPUT_FILE_NAME = "B-large.in"

# OUTPUT_FILE_NAME = "B-sample.out"
# OUTPUT_FILE_NAME = "B-small-attempt1.out"
OUTPUT_FILE_NAME = "B-large.out"

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
        w1 = read_word(input_file)
        args = {'N': w1}

        print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        print(out)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
