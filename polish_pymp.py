import math

function_map = {'+': lambda a, b: a + b,
                '-': lambda a, b: a - b,
                '*': lambda a, b: a * b,
                '/': lambda a, b: a / b,
                '^': lambda a, b: a ** b,
                '%': lambda a, b: a % b}

def parse(tokens):
    """ Recursively parses polish notation"""

    return function_map[tokens[0]](*[parse(tokens[arg_n+1:]) if type(tokens[arg_n+1]) != int else tokens[arg_n+1] for arg_n in range(2)])


def lex(string):
    return [int(x) if x.isdigit() else x for x in string.split(' ')]

l = "+ 22 / 19 ^ 2 9"
print("tokens:", lex(l))
print("result:", parse(lex(l)))
# >> 22.037109375