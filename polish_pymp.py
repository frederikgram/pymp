def parse(tokens):
    """ Recursively parses polish notation"""

    args = [parse(tokens[arg_n+1:]) if type(tokens[arg_n + 1]) != int else tokens[arg_n + 1] for arg_n in range(2)]
    return eval("{0}{1}{2}".format(args[0], tokens[0], args[1]))


def lex(string):
    return [int(x) if x.isdigit() else x for x in list(string)]

l = "+2*42-42/23"
print(parse(lex(l)))
# >> 10