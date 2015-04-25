import itertools
import re

__author__ = 'david'


#
# for i in range(0,3,3):
#     print("%s" % i)
#
#
#
# case = 1
# words = ["111111","2222","3333","444","555555","6"]
# print("Case #%d: %s\n" % (case,' '.join(words[::-1])))


# v1 = [1, 3, -5]
# v2 = [-2, 4, 1]
#
# v1.sort()
# v2.sort()
#
# print(v1, v2)
#
# v2 = v2[::-1]
#
# print(v1, v2)
#
# print(sum([x*y for x in v1 for y in v2]))


# str = "this is s(ing ex)8(ample....wow!!! this is really string";
# print(str.replace("(", "["))

# s = "Split string by the occurrences of pattern. If capturing parentheses are used in pattern, then the text of all groups in the pattern are also returned as part of the resulting list. If maxsplit is nonzero, at most maxsplit splits occur, and the remainder of the string is returned as the final element of the list. (Incompatibility note: in the original Python 1.5 release, maxsplit was ignored. This has been fixed in later releases.)"
# s = s.split("a")
# l = []
# for i in s:
#     l.append(i.split("e"))

# l = list("123456789")
# print(l[1::2])
# l.pop(0)
# print(l)
# print(l.pop(3))
# print(l)
#
# m = [2]
# l += m
# print(l)

# s = list(range(29))
# s.append(2)
# print(s)
# s.sort()
# print(s)

# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# for index, i in enumerate(seasons):
#     print(index,i)


# horses = [1, 2, 3, 4]
# print("horses",horses)
# races = itertools.combinations(horses,2)
# print("combinations",list(races))
# races = itertools.permutations(horses)
# print("permutations",list(races))
# races = itertools.product(horses)
# print("product",list(races))

# horses = [1,2,3,4]
# print("horses",horses)
# # races = itertools.combinations(horses,2)
# # print("combinations",list(races))
# races = itertools.permutations(horses)
# print("permutations",list(races))


# to_switch = range(10)
# for L in range(0, len(to_switch)+1):
#     for subset in itertools.combinations(to_switch, L):
#         print(subset)

# tuples = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]
# tuples = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)]
#
# print(sorted(tuples, key=lambda c: c[0]+c[1]))
# print(tuples)
# tuples.sort(key=lambda c: c[0]+c[1])
# print(tuples)
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


# file = open("italy.txt", "r")
#
# line = next(file).strip()
#
# patt = r"<img src=\"([^<]+)\" class=\"player\"></a></div></div><div class=\"p-n\"><a href=\"[^<]+\">"
# patt += r"<span class=\"p-n-webname\">([^<]+)</span></a><span class=\"p-i-fieldpos\">([^<]+)</span><span class=\"p-i-clubname\">([^<]+)</span>"
# patt += r"</div><div class=\"p-ag\"><span class=\"p-i-age\">Age </span><span class=\"p-i-birthdate\" data-attr=\"[-\w]+\">([^<]+)</span></div><div class=\"p-wh\"><span class=\"p-i-width-height\">([0-9]+) - ([0-9]+)</span>"
#
# players = re.findall(patt, line)
#
# for player_data in players:
#
#     print(player_data)
#
# file.close()


# a = lambda b: b * 2
# b = lambda c: a(c) / 4
# c = 4
# c = a(c)
# c = b(c)
# c = a(c)
# print(int(c))

# l = ['bosca', 'dosdos', 'apellizz', 'bugant', 'bugman', 'eitch', 'serex', 'chritchens', 'giulio', 'culo', 'johnny', 'teoti',]

import random

# random.shuffle(l)
# print [(l[x], l[x + 1]) for x in range(0, len(l)-1, 2)]


def print_args(p, *args):
    print('param: ', p, '\nargs: ',)
    for a in args: print(a,)


print_args("ciao", ('A', 'B', 'C'), 3, 2.5, 'hello')


def print_kwargs(f, g, **kwargs):
    # Check for a key
    m = kwargs['m'] if 'm' in kwargs else None
    if m: print("Value '%s' founded for key '%s'! :)" % (str(m), str(kwargs['m'])))
    # Print all keys
    for k in kwargs.keys(): print(kwargs[k])


print_kwargs("ciao", "mondo", m="amico", n="mio", t="Tony")
args = {'m': "amico", 'n': "mio", 't': "Tony"}
print_kwargs(1, 2, **args)