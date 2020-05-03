"""
Created on 04/04/2020

@author: Dos

Problem B. Nesting Depth
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f

***Sample***

Input
4
0000
101
111000
1

Output
Case #1: 0000
Case #2: (1)0(1)
Case #3: (111)000
Case #4: (1)

"""


def solve(case, s):
    result = '(' * int(s[0])
    for i in range(len(s)-1):
        result += s[i]
        diff = int(s[i]) - int(s[i+1])
        if diff > 0:
            result += ')' * diff
        elif diff < 0:
            result += '(' * (-1 * diff)
    result += s[-1] + ')' * int(s[-1])
    return "Case #{}: {}".format(case, result)


T = int(input())
for t in range(1, T+1):
    S = input()
    print(solve(t, S))

# s = '111000'
# print(s, solve(1, s))
# s = '0000'
# print(s, solve(2, s))
# s = '101'
# print(s, solve(3, s))
# s = '1'
# print(s, solve(4, s))
# s = '312'
# print(s, solve(5, s))
# s = '912343003'
# print(s, solve(6, s))
