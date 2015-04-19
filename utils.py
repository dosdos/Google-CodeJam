###################
#  PARSE STRINGS  #
###################


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


###############
#  GDC & LCM  #
###############

def gcd(n, m):
    while m:
        n, m = m, n % m
    return n


def lcm_couple(n, m):
    return n * m // gcd(n, m)


def lcm(*args):
    return reduce(lcm_couple, args)
