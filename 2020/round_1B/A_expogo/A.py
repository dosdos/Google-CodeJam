"""
Created on 19/04/2020

@author: Dos

Problem A. Expogo
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b62

***Sample***

Input
4
2 3
-2 -3
3 0
-1 1

Case #1: SEN
Case #2: NWS
Case #3: EE
Case #4: IMPOSSIBLE

"""

steps = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296, 8589934592, 17179869184, 34359738368, 68719476736, 137438953472, 274877906944, 549755813888]


def get_idx(n):
    i = 0
    while n >= steps[i]:
        i += 1
    return reversed(steps[:i])


def solve(case, x, y):
    sum_xy = abs(x) + abs(y)
    if sum_xy % 2 == 0:
        result = 'IMPOSSIBLE'
    else:
        result = ''
        for i in get_idx(sum_xy):
            if abs(x) > abs(y):
                if x > 0:
                    x -= i
                    result = 'E' + result
                else:
                    x += i
                    result = 'W' + result
            else:
                if y > 0:
                    y -= i
                    result = 'N' + result
                else:
                    y += i
                    result = 'S' + result
    return "Case #{}: {}".format(case, result)


T = int(input())
for t in range(1, T+1):
    x, y = input().split()
    print(solve(t, int(x), int(y)))
