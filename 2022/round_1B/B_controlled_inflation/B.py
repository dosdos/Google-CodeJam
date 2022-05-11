"""
Created on 24/04/2022

@author: Dos

Problem B. Controlled Inflation
https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000accfdb

***Sample***

Sample Input
2
3 3
30 10 40
20 50 60
60 60 50
5 2
1 1000000000
500000000 1000000000
1 1000000000
500000000 1
1 1000000000

Sample Output
Case #1: 110
Case #2: 4999999996

"""


def solve(case, num_of_clients, num_of_products, clients):
    inflation_level = max(clients[0])
    tot_inflation = inflation_level

    for client in clients[1:]:
        curr_min = min(client)
        curr_max = max(client)
        tot_inflation += curr_max - curr_min

        inflation_level = min(
            abs(inflation_level-curr_min),
            abs(inflation_level-curr_max),
        )

        tot_inflation += inflation_level

    tot_inflation -= inflation_level

    print(f"Case #{case}: {tot_inflation}")


T = int(input())
for t in range(1, T+1):
    N, P = map(int, input().split(' '))
    targets = []
    for _ in range(N):
        targets.append(list(map(int, input().split(' '))))
    solve(t, N, P, targets)
