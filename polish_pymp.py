def parse(tokens):
    """ Recursively parses polish notation"""

    return eval("{1}{0}{2}".format(tokens[0], *[parse(tokens[arg_n+1:]) if type(tokens[arg_n+1]) != int else tokens[arg_n+1] for arg_n in range(2)]))


def lex(string):
    return [int(x) if x.isdigit() else x for x in string.split(' ')]

l = "+ 22 / 19 ^ 2 9"
print("tokens:", lex(l))
print("result:", parse(lex(l)))
# >> 23.727272727272727