"""
Created on 04/04/2020

@author: Dos

Problem D. ESAb ATAd
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9e

"""
import sys


def solve(b):
    length = b + 1
    solution = [''] * length
    for i in list(sorted(list(range(1, length)) + list(range(1, length, 9)))):
        print(i)
        sys.stdout.flush()
        solution[i] = input()
    print(''.join(solution))
    result = input()
    if result == "Y":
        return


T, B = map(int, input().split())
for _ in range(T):
    solve(B)


# import sys
#
#
# def solve(b):
#     sys.stdout.flush()
#     length = b + 1
#     solution = [''] * length
#     for i in range(1, length):
#         print(i)
#         solution[i] = input()
#     print(''.join(solution))
#     result = input()
#     if result == "Y":
#         return
#
#
# T, B = map(int, input().split())
# for _ in range(T):
#     solve(B)
