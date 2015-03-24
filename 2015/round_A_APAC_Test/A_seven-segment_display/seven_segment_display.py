"""
Created on 03/05/apr/2014

@author: dosdos

Problem A. Seven-segment Display
https://code.google.com/codejam/contest/3214486/dashboard


***Sample***

Input
1 1111111
2 0000000 0001010
3 0100000 0000111 0000011
5 1011011 1011111 1010000 1011111 1011011

Output
Case #1: 1110000
Case #2: ERROR!
Case #3: 0100011
Case #4: 0010011

"""

numbers = {
    '1111110': 0,
    '1101101': 2,
    '1111001': 3,
    '0110011': 4,
    '1011011': 5,
    '1011111': 6,
    '1110000': 7,
    '1111111': 8,
    '1111011': 9,
}

prev_nums = {
    '1111110': '1111011',  # 0
    '1101101': '1111110',  # 2
    '1111001': '1101101',  # 3
    '0110011': '1111001',  # 4
    '1011011': '0110011',  # 5
    '1011111': '1011011',  # 6
    '1110000': '1011111',  # 7
    '1111111': '1110000',  # 8
    '1111011': '1111111',  # 9
}


def read_word(f):
    return next(f).strip()


def read_int(f, b=10):
    return int(read_word(f), b)


def read_words(f, d=' '):
    return read_word(f).split(d)


def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]


def read_decimals(f, d=' '):
    return [float(x) for x in read_words(f, d)]


def solve(file_in, file_out):
    # create I/O files
    input_file = open(file_in, 'r')
    output_file = open(file_out, "w")

    # read file size
    T = read_int(input_file)

    print("There are %d cases to solve! :)\n" % T)

    # iterate on each case
    for case in range(T):
        print("\nCase #%d: " % (case + 1))

        # get problem data
        line = read_words(input_file)
        N = int(line[0])
        nums = line[1:]
        print("%d %s" % (N, str(nums)))

        broken = False

        if len(nums) == 1:
            if nums[0] in numbers:
                print("Case #%d: %s\n" % (case, prev_nums[nums[0]]))
            else:
                # TODO: gestisci casi limite
                print("Case #%d: %s\n" % (case, "ERROR!"))

        else:
            broken_nums = []
            for i in range(7):
                if nums[0][i] == '0':
                    broken_nums.append(i)

            l = len(broken_nums)
            for i in range(N-1):
                for b in range(l):
                    print(broken_nums[b])
                    if nums[i+1][broken_nums[b]] == '0':
                        broken_nums.pop(broken_nums[b])

            print broken_nums

            print("Case #%d: %s\n" % (case, "ERROR!"))

        # prev = nums[0]
        # for n in nums[1:]:
        #     print(n)
        #     if n in numbers:
        #         print(numbers[n])
        #
        #         prev = n
        #
        #     else:
        #         broken = True
        #         break





        # print output data!
        # output_file.write("Case #%d: %d\n" % (case + 1, counter))

    # close I/O files
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    input_file_name = "A-sample.in"
    output_file_name = "A-sample.out"
    solve(input_file_name, output_file_name)
