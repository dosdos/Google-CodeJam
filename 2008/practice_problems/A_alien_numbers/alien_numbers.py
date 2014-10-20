'''
Created on 11/jan/2014

@author: david

Problem A. Alien Numbers
(link: http://code.google.com/codejam/contest/32003/dashboard#s=p0)


***Problem***

The decimal numeral system is composed of ten digits, which we represent as
"0123456789" (the digits in a system are written from lowest to highest).
Imagine you have discovered an alien numeral system composed of some number of
digits, which may or may not be the same as those used in decimal. For example,
if the alien numeral system were represented as "oF8", then the numbers one
through ten would be (F, 8, Fo, FF, F8, 8o, 8F, 88, Foo, FoF).
We would like to be able to work with numbers in arbitrary alien systems.
More generally, we want to be able to convert an arbitrary number that's written
in one alien system into a second alien system.

***Input***

The first line of input gives the number of cases, N. N test cases follow.
Each case is a line formatted as

            alien_number source_language target_language
            
Each language will be represented by a list of its digits, ordered from lowest
to highest value. No digit will be repeated in any representation, all digits in
the alien number will be present in the source language, and the first digit of
the alien number will not be the lowest valued digit of the source language (in
other words, the alien numbers have no leading zeroes). Each digit will either
be a number 0-9, an uppercase or lowercase letter, or one of the following
symbols

            !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

***Output***

For each test case, output one line containing "Case #x: " followed by the alien
number translated from the source language to the target language.

***Limits***

1 ≤ N ≤ 100.

***Small dataset***

1 ≤ num digits in alien_number ≤ 4,
2 ≤ num digits in source_language ≤ 16,
2 ≤ num digits in target_language ≤ 16.

***Large dataset***

1 ≤ alien_number (in decimal) ≤ 1000000000,
2 ≤ num digits in source_language ≤ 94,
2 ≤ num digits in target_language ≤ 94.

***Sample***


Input
4
9 0123456789 oF8
Foo oF8 0123456789
13 0123456789abcdef 01
CODE O!CDE? A?JM!.

Output
Case #1: Foo
Case #2: 9
Case #3: 10011
Case #4: JAM!

'''
import unittest


class AlienNumbers(object):
    
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


    def alien_to_int(self, n, language):
        
        n = str(n)
        base = len(language)
        
        if n == 0:
            return language[0]
        
        s = 0
        i = 0
        for cipher in n[::-1]:
            s += (base ** i ) * language.index(cipher)
            i += 1
        
        return s
    
    
    def int_to_alien(self, n, language):
        
        try:
            n = int(n)
            n = abs(n)
            base = len(language)
        except:
            return ""
        
        if n == 0:
            return language[0]
        
        s = ""
        while n != 0:
            r = n % base
            s = language[r] + s
            n = int(n / base)
        
        return s
        
    
    def solve(self):
        
        # create I/O files
        input_file = open(self.input_file_name, 'r')
        output_file = open(self.output_file_name, "w")
        
        # read file size
        T = self.read_int(input_file)
        
        # initialize cases to 1
        case = 1
        
        # iterate on each line
        for l in range(T):
            
            line = self.read_words(input_file)
            # get problem data
            alien_number = line[0]
            source_language = line[1]
            target_language = line[2]

            # transform the alien number from source language to int
            int_number = self.alien_to_int(alien_number, source_language)
            
            # transform the int number from int to target language
            target_number = self.int_to_alien(int_number, target_language)
            
            output_file.write("Case #%d: %s\n" % (case, target_number))
            case += 1
        
        # close I/O files
        input_file.close()
        output_file.close()


class Test(unittest.TestCase):

    def setUp(self):
        self.alien_numbers = AlienNumbers()

    def test_alien_to_int(self):
        self.assertEqual(self.alien_numbers.alien_to_int('12343','012345'), 1863)
        self.assertEqual(self.alien_numbers.alien_to_int('23','0123'), 11)
        self.assertEqual(self.alien_numbers.alien_to_int('241','01234'), 71)
        self.assertEqual(self.alien_numbers.alien_to_int('100101','01'), 37)
        self.assertEqual(self.alien_numbers.alien_to_int('100101','012'), 253)
        self.assertEqual(self.alien_numbers.alien_to_int('10','0123456789abcdef'), 16)
        self.assertEqual(self.alien_numbers.alien_to_int('2ad','0123456789abcdef'), 685)
        self.assertEqual(self.alien_numbers.alien_to_int('100101','0123456789abcdefghijkl'), 5154117)

    def test_int_to_alien(self):
        self.assertEqual(self.alien_numbers.int_to_alien(4,'01'), '100')
        self.assertEqual(self.alien_numbers.int_to_alien(4,'ed'), 'dee')
        self.assertEqual(self.alien_numbers.int_to_alien(1863,'012345'), '12343')
        self.assertEqual(self.alien_numbers.int_to_alien(1863,'retj6+'), 'etj6j')

    def test_solve(self):
        an_sample = AlienNumbers("B-sample.in", "B-sample.out")
    #     an_sample = AlienNumbers("A-small-practice.in", "A-small-practice.out")
    #     an_sample = AlienNumbers("A-large-practice.in", "A-large-practice.out")
        an_sample.solve()


if __name__ == '__main__':
    unittest.main()
