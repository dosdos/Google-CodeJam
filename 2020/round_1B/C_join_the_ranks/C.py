"""
Created on 19/04/2020

@author: Dos

Problem C. Join the Ranks
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b64

***Sample***

Input
3
3 2
3 3
3 4

Output
Case #1: 1
2 1
Case #2: 2
3 2
2 1
Case #3: 2
2 3
2 2

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
