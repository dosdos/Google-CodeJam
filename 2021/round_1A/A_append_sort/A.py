"""
Created on 29/04/2020

@author: Dos

Problem A. Append Sort
https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/00000000007549e5

***Sample***

Input
4
3
100 7 10
2
10 10
3
4 19 1
3
1 2 3

Output
Case #1: 4
Case #2: 1
Case #3: 2
Case #4: 0
"""


def get_new_curr(prev, curr):
    original = curr
    if len(prev) > len(curr):
        curr += '0' * (len(prev) - len(curr))
    if int(curr) > int(prev):
        return curr
    else:
        return curr + '0'
        # if not int(original + '9' * (len(prev) - len(original))) > int(prev):
        #     return original + '0'
        # else:
        #     return str(int(prev) + 1)


def solve(case, size, elements):
    """
    :param case: the numeric ID of the current test case
    :param size: number N of integers in the list
    :param elements: list that contains N str integers X1,X2,…,XN, the members of the list.
    :return: string to print with the solution
    """
    min_changes = 0  # min num of single digit append operations needed for the list to be in strictly increasing order
    prev = elements[0]
    for e in elements[1:]:
        if not int(e) > int(prev):
            curr = get_new_curr(prev, e)
            # print(curr, e)
            min_changes += len(curr) - len(e)
        else:
            curr = e
        prev = curr
    return "Case #{}: {}".format(case, min_changes)


T = int(input())
for t in range(1, T+1):
    N = input()
    X = input().split()
    print(solve(t, int(N), X))
