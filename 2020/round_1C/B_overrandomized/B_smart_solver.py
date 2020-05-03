"""
Created on 02/05/2020

@author: Dos

Problem B. Overrandomized
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef4/00000000003179a1
***Sample***

Input
see B-sample.in file

Output
Case #1: TPFOXLUSHB

"""

T = int(input())
for t in range(1, T+1):
    U = input()
    counter = dict()
    all_unsorted = set()
    for _ in range(10**4):
        max_n, rand = input().split()
        first_letter = rand[0]
        counter[first_letter] = counter.get(first_letter, 0) + 1

        if len(all_unsorted) < 10:
            for letter in rand:
                all_unsorted.add(letter)

    result = ''.join([l for l, occ in sorted(counter.items(), key=lambda x: x[1])])
    result += (all_unsorted - set(result)).pop()

    print("Case #{}: {}".format(t, result[::-1]))
