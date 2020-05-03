"""
Created on 19/04/2020

@author: Dos

Problem B. Blindfolded Bullseye
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b63

"""


def solve(case, s):
    result = '' + s
    return "Case #{}: {}".format(case, result)


T = int(input())
for t in range(1, T+1):
    S = input()
    print(solve(t, S))
