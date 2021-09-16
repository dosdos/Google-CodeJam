"""
Created on 26/03/2021

@author: Dos

Problem E. Cheating Detection
https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1155

***Sample***

Sample Input
1
0
0011101000101010000010000001000101010000000011000110101000100001100101010000011000010010001000011000010010000000000010010000000000000111000110001010000000011110010000011001111000101011001100010000010000000010000100100000000000001000011010000101010000000000010001001111000100010001000000010011010001001100110000100010001000010100000001001100010000010000011110010000000110000001001100100001000110000001000000100000001011000100010001101000000000000000000000001110010000001010010101101000011000000000000001000100001011000000110100100000000011100000010000000111100001000010000000000000110111101100110000111100100000100000011011010110000011000000001000100101000010000110010010010001000000110101001000001000100000010001010010001000100000000110110001000000110001000000000000000011010000100010000000110100010001001010110000000001000000010000000011100000001010101000000100000110000001000011001100010001111010100101010000000000100000100100000000011101000000000100101100001000000000101000110100000001010001111100001000000100001111000011100001000001100000000011011000001000100110110000000001111000100000001000011011010000000000001011100000000110000011001010000001010000011000100001000001010000010000000001100010000001100000000000001001000010010000000000010000110000000110000000100000100010000100000011010010001000010000001100011001001101110010010110000101111100000011000011011000000010000010101101100100010000001000000101100000010000101000001000100000000100000111010000000011001011011001100010001000000001111000100100001000000010000000100000101000000000000001100000111100100010001010000110000001010100010100011010010000010000100000100000010010010000110000111100100111110000001000100000000001000001000000000000110001100010000000110100001000010011001110010000001000000000000100000010000100000000101000110010001011000001000100111000010101001000011100000010011100000100100111100100000000000011001000110000000000000010110100010001000000000100000100010100001000010000010101000001111000110000010011100000000000000010100000000100000000011010100001100010001000000000111000001100000000010101010000000011001000001010000110110000111010001100000100000001110000000000000001001000000000010001000000000000001100010001100000010000000000000000101000000000000000100010110000010100110001000010010001011100110001000100100000010000001001101010000101000110000101000000010010000000100110000001000000100010000001101001001100010000000100110001100010000000100100001010010000010000001000000000000000001000000001110010010000101110001100010010100000111001000000000000110100110101010100000000101000000001100000000010111001000101010000000001010000000000101000000000010000000000010100101110010100000001101000010100100010000000101000001001100001010110000010000110001000100000000010010001000011011100000001001100100000000111001000100010000011100100000110100001010010001000110001001100100001000000110111010000000001000000000100010100000011010010000000100111000000000000000000010101100011000011101000000000001001000100100010111101000100110111010100010001000000000011011000010000001100000000010100000001001000110001011000100000000011010010000100111101110000011100000110100001000110000100101010100001100010010100000000010001000000001001110000010000000110000100010010000111100100000000000000101000010010001001000110010001001101000001001001000000000100000010001101000000010101010001010001110010100000000010101000011001001100000100101000010000101000001101111001000110000000000001011000011001000000100001000010000000000100000100011001001110010010000111100010000010001000001100010000001000101000010010010000011001101010110001000001001000101110010010100000000000001100010000001010000101000110000001001110010101000000100000000000000010001001000010010000010001001000000000011000110000001000001111000000000000001000101100001000000100010101001111011000100000100000100001110101001000100000000100010011010010000000000000100110000001001010101001110011110000000010001100000101000000000111100000000001100101001000000000000000000000000101000010110000110001000101100000000000000000000100000000001011000011001000000000000011001111001000000001000011000001100011100000000000111100000001000000010001100100000001000010000001010001100010000100001001011101000100100000000011010000100000011001000011101010000010010010100100011000100001000110001110000100100010100100010010110111010001100000100010000000001010111100011001010000000000000100001001011000000100010001111000010000010100001010100001010010101000010100000010001100010000010101000010010100011111110111000010010000010000000000000010100110001000100010000101100100100010001000001000100010000010000101010011000100110000011010000010110000011000000010100010010101100010010000010001101000000000000010001101000000000000000101001000000001011000000000000000101010110001000100000011000000100010000000001101011000000100100000001010000010010010000101000001100001100100110000000100010001010100000011000000001010000000000110010101011000010000000000000100011000000010101011000001011000011000000010000010001010000011100010100000001110000000000001100101000001100110000011000000101000101001000001011000100100000100010100000011100110101000000011010011001100011100011010100010100111100000000010111101000011000010000000001101010100000011000000000000101000000001001000000000100001100001101010001000010001000001000100000000010101000010010000111000010000000000001000000011110011000010010000000000101100000100010001101000000000010110100010100111001000000100000000001100010010000011010110000010100101001000001101000001100001101010000100010011101000000001100100000100010101000000000011000000000100000100010101010010000000010001010000100010000001010000101100001000000001000100000100101101000100111000000000000100110000101001000010000110101000010101000110000010100001000011101111000000110010000110110100000000010000001010001011000100000000000110100000110110010110000100101000000000000001001100010101000000010000000010000110001000000001010001000000101000010010010101101100000001001001001110010001111011000000100000100010000100010111001000000000100010000000110111001001100000000100011100100000000010010001000110010101101011000000100000101011001100000000101000000000010100101100000100110100001000011010010000000000000011101001000111000000000001010001001000000001000000010000000011000000100000110011000001100100010000000100000000010000100000000101010101000001001000011000001010111000000011101101011110000010000000000011000000000100010000110000000010001100011001100000110000000010000000001010011000011010011000010001100000000100011001000010000010010000110100010011000000000000100101000000010111000000000001000001001001010000001000000000000010010000001001001001100010101000000011010010001000100000000100001111000100110000100100000101000100001000001000010000010011000000000100100100010000110000000101001000010100000010000101010000000000101011000000010000000010000000010100001100000000000111000001011101001001000110000100000010000010000100000000010011101000110000010011000100110000100000000000000100100010111010010010010000000111000000001000101110010101000110100111000000001010000100010000000010001000001010000110000100001010011101010010100000000000010100000010000110000010001000001000011000010010000000011100111101011000100010000000000010000000000000100000000100010001110101101010111000000101101100000111001010000000011010110100000000010000000001100000000001000010100100010010000011100001100110100000010100010100000000000010100010001010000110001000000001000010100011000000100000011000100000000100000110000001000101000000011001001010000000101000000001000100010010000100011100001010000001100010000000100000100101100101000000000010001000000111100110000101100000110000000100010000010010010100000111000011001001100000110000100000001101011011010000100000100000100110000100101000010000010100000001001000000100011000000110011001100000010000001001010001000100001000000000100000100001000000001001001001011001010011100100001000101011001001101100110000000000000000000000010000000010001000100010000101101000010001001001111000000001000001110000000001000000000011000011000000000000011000000000000110000000001001101000000100000001000001100010010010000010000000010100010010000011001001010010000000000000000000001100111011000000001010111100000000000000101001010000100100000011000001111000010001000001100010001011000000100110000100000101000000001001000000000010111000100100000100010000000000000010100000100010000000001011010110010101000001000000000000001011011001100000001000000000000000000000101000001001110100000000001000000111101001100000000010011000100010001000001100100100001100100010001100001010101010001010001001000010100000000000000000000000000010100100101000110000001001000001001110110001000001001000000010000111001111001010001101010111000010010001101001000100101100000110000000010010010000100100000000011001001011000001000001110010011000000110000000001010000100001000010010001010111001000001010000001111000100100100000110010000101100000110100000000010000000100100010000010000101110001000000000000100101000000000110011001011100111000001100000001000111000011000000100101000001010010110000000000000110010001010001010110100000001101100111011111000000010000001100001001110001001101011000000000100000010001000000101001001000001000000000000111000100010000000010001000000001000000000000000101000000000000110010100010001001001000001100010000000101100000000000110010000100010000000000010111101110001011100000001011000101011010001100001100101000000000100000000000100000010000100000001000000010001000100100001110100010101100000100010001000010110000000000000101000000000001001000000111001000011011010101110010100000000011110000100000110010000000010011110001011010000000000100011001000000010000010011000000001011000000000000011010001000101000010111000001001001001011000000000000010011000000101000010100100000001011110000100001100010110000011001010001010100000010011101100010000000100100000000101101000100100001000000010001000000000000010100110000000100010110000000000000100001011010001111100000010000011000000110000000000100000100001000100000001001100100101010101010000101000100110
-------------------------------
99 lines of input omitted.
Use the download button above
to view the full sample input.
-------------------------------

Sample Output
Case #1: 59


"""


def count_zeros_and_ones(zeros_and_ones):
    zeros = 0
    ones = 0
    for c in zeros_and_ones:
        if c == '0':
            zeros += 1
        if c == '1':
            ones += 1
    return zeros, ones


players = 100
T = int(input())
P = input()
for case in range(1, T+1):
    cheater = 0
    cheater_score = 0
    for i in range(players):
        current_player = i + 1
        answers = input()
        zero_count, one_count = count_zeros_and_ones(answers)
        curr_score = one_count - zero_count
        if curr_score > cheater_score:
            cheater_score = curr_score
            cheater = current_player
    print(f"Case #{case}: {cheater}")
