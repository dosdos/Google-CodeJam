import unittest

input_file = open('D-large.in', 'r')
number_of_tests = input_file.readline()

result_file = open("D-large.out", "w")


def get_x_r_c(line):
    return int(line.split()[0]), int(line.split()[1]), int(line.split()[2])


def who_wins(x, r, c):
    if x < 7:
        if (r * c) % x == 0:
            if r >= x or c >= x:
                if x % 2 == 0:
                    if (r >= x/2 + 1 and c >= x/2 + 1 - 1) or (c >= x/2 + 1 and r >= x/2 + 1 - 1):
                        if x <= 3:
                            return "GABRIEL"
                        if r * c >= 3 * x:
                            return "GABRIEL"
                else:
                    if (r >= (x + 1)/2 and c >= (x + 1)/2) or (c >= (x + 1)/2 and r >= (x + 1)/2):
                        if x <= 3:
                            return "GABRIEL"
                        if r * c >= 3 * x:
                            return "GABRIEL"

    return "RICHARD"


for j in range(int(number_of_tests)):
    x, r, c = get_x_r_c(input_file.readline())
    print "x:{} r:{} c:{}".format(x, r, c)

    print "Case #{}: {}\n".format(j + 1, who_wins(x, r, c))
    result_file.write("Case #{}: {}\n".format(j + 1, who_wins(x, r, c)))

input_file.close()
result_file.close()


class MyTestCase(unittest.TestCase):

    def test_calculate_guest_to_add(self):
        self.assertEqual(who_wins(2, 2, 2), "GABRIEL")
        self.assertEqual(who_wins(2, 1, 3), "RICHARD")
        self.assertEqual(who_wins(4, 4, 1), "RICHARD")
        self.assertEqual(who_wins(3, 2, 3), "GABRIEL")
        self.assertEqual(who_wins(2, 4, 1), "GABRIEL")
        self.assertEqual(who_wins(3, 3, 1), "RICHARD")

if __name__ == '__main__':
    unittest.main()
