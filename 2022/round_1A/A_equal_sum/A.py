"""
Created on 24/04/2022

@author: Dos

Problem A. Equal Sum
https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa8fc1
"""

import sys


def solve(numn_list):
    return numn_list[:5]


def format_ints(arr):
    return ' '.join(map(str, arr))


T = int(input())
for _ in range(T):
    N = int(input())
    print(N)
    my_numbers = list(range(1, N+1))
    print(format_ints(my_numbers))
    sys.stdout.flush()
    new_numbers = list(map(int, input().split()))
    solution = solve(my_numbers + new_numbers)
    print(format_ints(solution))
    sys.stdout.flush()
