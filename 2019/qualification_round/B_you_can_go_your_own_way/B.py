#!/usr/bin/env python3

"""
Created on 06/04/2019

@author: Dos

Problem B. You Can Go Your Own Way
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

***Sample***

Input
2
2
SE
5
EESSSESE

Output
Case #1: ES
Case #2: SEEESSES

"""


def solve(case, **kwargs):
    P = kwargs['P']
    result = ''
    for i in P:
        result += 'E' if i == 'S' else 'S'

    return "Case #{}: {}".format(case, result)


T = int(input())
for case in range(1, T+1):
    N = int(input())
    P = input()
    args = {'N': N, 'P': P}
    print(solve(case, **args))
