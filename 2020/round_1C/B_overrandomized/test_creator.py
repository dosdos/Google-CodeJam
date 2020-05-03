import random


U = 16
T = 1
CRYPTO = 'QWERTYUIOP'
UPPER = 10**U - 1
LINES = 10*1

output_file = open("sample.in", "w")
output_file.write(f'{str(T)}\n')

for t in range(T):
    output_file.write(f'{str(U)}\n')
    for _ in range(10**4):
        max_rand = random.randint(1, UPPER)
        rand_n = random.randint(1, max_rand)
        crypto_n = ''.join([CRYPTO[int(c)] for c in str(rand_n)])
        # print(f'{max_rand} {crypto_n}')
        output_file.write(f'{max_rand} {crypto_n}\n')

output_file.close()
