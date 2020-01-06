"""
Created on 07/04/2018

@author: Dos

Problem C. Cryptopangrams
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b

***Sample***

Input
2
103 31
217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053
10000 25
3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543

Output
Case #1: CJQUIZKNOWBEVYOFDPFLUXALGORITHMS
Case #2: SUBDERMATOGLYPHICFJKNQVWXZ

"""
AZ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PRIMES = []
for n in range(101, 10000):
    if all(n % i!=0 for i in range(2, n)):
        PRIMES.append(n)


def get_max_prime(n):
    for i in reversed(PRIMES):
        if i <= n:
            return i
    return PRIMES[0]


def get_last_prime(n, val_list):
    for _ in range(len(PRIMES)):
        n = get_max_prime(n)
        for v in val_list:
            if v % n == 0:
                return n
        n -= 1


def solve(case, **kwargs):
    N = kwargs['N']
    values = kwargs['values']
    result = []

    n = get_last_prime(N, values)

    multipliers = {}
    primes = [n]

    for curr in primes:
        for v in values:
            if v not in multipliers and v % curr == 0:
                v2 = v // curr
                multipliers[v] = (curr, v2)
                if v2 not in primes:
                    primes.append(v2)

    primes = sorted(primes)

    for v in values:
        result.append(multipliers[v])

    for i in range(len(result)-1):
        if result[i][0] in result[i+1]:
            result[i] = (result[i][1], result[i][0])
    if result[-1][1] in result[-2]:
        result[-1] = (result[-1][1], result[-1][0])

    final = [result[0][0]]
    for r in result:
        final.append(r[1])

    pangram = ''
    for f in final:
        pangram += AZ[primes.index(f)]

    return "Case #{}: {}".format(case, pangram)


T = int(input())
for case in range(1, T+1):
    N, L = [int(s) for s in input().split(" ")]
    values = [int(s) for s in input().split(" ")]
    args = {'N': N, 'L': L, 'values': values}
    print(solve(case, **args))
