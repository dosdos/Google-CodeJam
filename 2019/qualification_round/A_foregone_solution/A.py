#!/usr/bin/env python3

"""
Created on 06/04/2019

@author: Dos

Problem B. Foregone Solution
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231

***Sample***

Input
3
4
940
4444

Output
Case #1: 2 2
Case #2: 852 88
Case #3: 667 3777

"""


def solve(case, **kwargs):
    N = kwargs['N']
    a = b = ''
    for i in N:
        a += '1' if i == '4' else '0'
        b += '3' if i == '4' else i
    return "Case #{}: {} {}".format(case, a.lstrip('0'), b)


T = int(input())
for case in range(1, T+1):
    N = input()
    args = {'N': str(N)}
    print(solve(case, **args))
