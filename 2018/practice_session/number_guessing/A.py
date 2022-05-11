"""
Created on 23/04/2022

@author: Dos

Practice Session 2018: Number Guessing
https://codingcompetitions.withgoogle.com/codejam/round/0000000000000130/0000000000000523

"""
import sys


def solve(a, b):
    m = (a + b) // 2
    print(m)
    sys.stdout.flush()
    s = input()
    if s == "CORRECT":
        return
    elif s == "TOO_SMALL":
        a = m + 1
    else:
        b = m - 1
    solve(a, b)


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    _ = int(input())
    solve(a + 1, b)
