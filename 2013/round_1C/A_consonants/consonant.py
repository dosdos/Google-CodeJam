"""
Created on 09/04/apr/2015

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
import math

vowels = "aeiou"


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


def has_at_least_n_consecutive_consonants(s, n):
    if len(s) < n:
        return False
    else:
        max = 0
        i = 0
        for c in s:
            if c in vowels:
                i = 0
            else:
                i += 1
                if i > max:
                    max = i
            if max >= n:
                return True

    return False


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
        word = line[0]
        num = int(line[1])
        print("%d %s" % (num, str(word)))

        counter = 0

        # Check on word len
        if len(word) >= num:

            # Check if word contains at least a vowel
            if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word:

                for i in range(len(word)):
                    for j in range(i+1, len(word)+1):
                        # print word[i:j]
                        if has_at_least_n_consecutive_consonants(word[i:j], num):
                            # print word[i:j]
                            counter += 1
                    # print word[:i], word[i:]

            else:
                counter = len(word)

        # print output data!
        print("Case #%d: %s\n" % (case + 1, counter))
        output_file.write("Case #%d: %d\n" % (case + 1, counter))

    # close I/O files
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    # input_file_name = "A-sample.in"
    input_file_name = "A-small-practice.in"
    # input_file_name = "A-large-practice.in"

    # output_file_name = "A-sample.out"
    output_file_name = "A-small-practice.out"
    # output_file_name = "A-large-practice.out"

    solve(input_file_name, output_file_name)
    # print has_at_least_n_consecutive_consonants("trwhy", 2)
