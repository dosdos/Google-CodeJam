"""
Created on 02/05/2020

@author: Dos

Problem C. Oversized Pancake Choppers
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef4/00000000003172d1

***Sample***

Input
4
1 3
1
5 2
10 5 359999999999 123456789 10
2 3
8 4
3 2
1 2 3

Output
Case #1: 2
Case #2: 0
Case #3: 1
Case #4: 1

"""


def solve(case, r, s):
    res = ''
    for i in range((r-1) * (s-1)):
        res += '\n{} {}'.format(r, (r-1) * (s-1) - i + 2)
    return "Case #{}: {}".format(case, res)


T = int(input())
for t in range(1, T+1):
    r, s = input().split()
    print(solve(t, int(r), int(s)))
