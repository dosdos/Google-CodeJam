"""
Created on 02/04/2022

@author: Dos

Problem A. Punched Cards
https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1

***Sample***

Input
3
3 4
2 2
2 3

Output
Case #1:
..+-+-+-+
..|.|.|.|
+-+-+-+-+
|.|.|.|.|
+-+-+-+-+
|.|.|.|.|
+-+-+-+-+
Case #2:
..+-+
..|.|
+-+-+
|.|.|
+-+-+
Case #3:
..+-+-+
..|.|.|
+-+-+-+
|.|.|.|
+-+-+-+

"""


def solve(case, rows, cols):
    print(f"Case #{case}:")
    print('..'+'+-'*(cols-1)+'+')
    print('..'+'|.'*(cols-1)+'|')
    for _ in range(rows-1):
        print('+-'*cols+'+')
        print('|.'*cols+'|')
    print('+-'*cols+'+')


T = int(input())
for t in range(1, T+1):
    R, C = input().split(' ')
    solve(t, int(R), int(C))
