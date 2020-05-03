"""
Created on 02/05/2020

@author: Dos

Problem B. Overrandomized
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef4/00000000003179a1
***Sample***

Input
see B-sample.in file

Output
Case #1: TPFOXLUSHB

"""

T = int(input())
for t in range(1, T+1):
    U = input()
    all_unsorted = set()
    first_letters = set()
    d_sets = {
        '1': set(),
        '2': set(),
        '3': set(),
        '4': set(),
        '5': set(),
        '6': set(),
        '7': set(),
        '8': set(),
        '9': set(),
    }
    for _ in range(10**4):
        max_n, rand = input().split()
        if len(first_letters) < 9 and rand[0] not in first_letters:
            first_letters.add(rand[0])
        if len(max_n) == 1:
            d_sets[max_n].add(rand)
        elif len(all_unsorted) < 10:
            for letter in rand:
                all_unsorted.add(letter)

    l0 = (all_unsorted - first_letters).pop() if len(first_letters) == 9 else (all_unsorted - d_sets['9']).pop()
    l1 = list(d_sets['1'])[0]
    l2 = (d_sets['2'] - d_sets['1']).pop()
    l3 = (d_sets['3'] - d_sets['2']).pop()
    l4 = (d_sets['4'] - d_sets['3']).pop()
    l5 = (d_sets['5'] - d_sets['4']).pop()
    l6 = (d_sets['6'] - d_sets['5']).pop()
    l7 = (d_sets['7'] - d_sets['6']).pop()
    l8 = (d_sets['8'] - d_sets['7']).pop()
    if len(d_sets['9']) == 9:
        l9 = (d_sets['9'] - d_sets['8']).pop()
    else:
        l9 = (all_unsorted - {l0, l1, l2, l3, l4, l5, l6, l7, l8}).pop()
    result = '{}{}{}{}{}{}{}{}{}{}'.format(l0, l1, l2, l3, l4, l5, l6, l7, l8, l9)
    print("Case #{}: {}".format(t, result))
