"""
Created on 06/apr/2014

@author: david

Problem A. Alien Language
(https://code.google.com/codejam/contest/90101/dashboard#s=p0)


***Problem***

After years of study, scientists at Google Labs have discovered an alien language
transmitted from a faraway planet. The alien language is very unique in that every word
consists of exactly L lowercase letters. Also, there are exactly D words in this language.

Once the dictionary of all the words in the alien language was built, the next breakthrough
was to discover that the aliens have been transmitting messages to Earth for the past decade.
Unfortunately, these signals are weakened due to the distance between our two planets and some
of the words may be misinterpreted. In order to help them decipher these messages, the scientists
have asked you to devise an algorithm that will determine the number of possible interpretations
for a given pattern.

A pattern consists of exactly L tokens. Each token is either a single lowercase letter (the
scientists are very sure that this is the letter) or a group of unique lowercase letters
surrounded by parenthesis ( and ). For example: (ab)d(dc) means the first letter is either
a or b, the second letter is definitely d and the last letter is either d or c.
Therefore, the pattern (ab)d(dc) can stand for either one of these 4 possibilities: add, adc, bdd, bdc.

***Input***

The first line of input contains 3 integers, L, D and N separated by a space.
D lines follow, each containing one word of length L.
These are the words that are known to exist in the alien language.
N test cases then follow, each on its own line and each consisting of a pattern as described above.
You may assume that all known words provided are unique.

***Output***

For each test case, output

Case #X: K
where X is the test case number, starting from 1, and K indicates how many words in the
alien language match the pattern.

***Limits***

***Small dataset***

1 ≤ L ≤ 10
1 ≤ D ≤ 25
1 ≤ N ≤ 10

***Large dataset***

1 ≤ L ≤ 15
1 ≤ D ≤ 5000
1 ≤ N ≤ 500

***Sample***

Input
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc

Output
Case #1: 2
Case #2: 1
Case #3: 3
Case #4: 0

"""
import re

__author__ = 'david'

import unittest


class AlienLanguage(object):

    def __init__(self, input_file_name=None, output_file_name=None):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name

    # file I/O
    def read_word(self, file):
        return next(file).strip()

    def read_int(self, file, b=10):
        return int(self.read_word(file), b)

    def read_words(self, file, d=' '):
        return self.read_word(file).split(d)

    def read_ints(self, file, b=10, d=' '):
        return [int(x, b) for x in self.read_words(file, d)]

    def language_to_regex(self, l):
        l = str(l)
        l = l.replace('(', '[')
        l = l.replace(')', ']')
        return l

    def solve(self):

        # create I/O files
        input_file = open(self.input_file_name, 'r')
        output_file = open(self.output_file_name, "w")

        # read file size
        first_line = self.read_ints(input_file)

        L = first_line[0] # words length
        D = first_line[1] # number of words
        N = first_line[2] # number of languages

        # initialize cases to 1
        case = 1

        print("There are %d cases to solve! :)\n\n" % N)

        # initializations
        words = []

        # iterate on each word
        for d in range(D):
            w = self.read_word(input_file)
            words.append(w)

        # iterate on each language
        for n in range(N):
            l = self.read_word(input_file)

            pattern = self.language_to_regex(l)
            count = 0

            for w in words:
                if re.search(pattern,w):
                    count += 1

            output_file.write("Case #%d: %d\n" % (case,count))

            case += 1

        # close I/O files
        input_file.close()
        output_file.close()


class Test(unittest.TestCase):
    def setUp(self):
        self.alien_language = AlienLanguage()

    def test_language_to_regex(self):
        self.assertEqual(self.alien_language.language_to_regex("(ab)(bc)(ca)"), "[ab][bc][ca]")
        self.assertEqual(self.alien_language.language_to_regex("abc"), "abc")
        self.assertEqual(self.alien_language.language_to_regex("(abc)(abc)(abc)"), "[abc][abc][abc]")
        self.assertEqual(self.alien_language.language_to_regex("(zyx)bc"), "[zyx]bc")

    def test_solve(self):
        # al_sample = AlienLanguage("B-sample.in", "B-sample.out")
        # al_sample = AlienLanguage("A-small-practice.in", "A-small-practice.out")
        al_sample = AlienLanguage("A-large-practice.in", "A-large-practice.out")
        al_sample.solve()


if __name__ == '__main__':
    unittest.main()
