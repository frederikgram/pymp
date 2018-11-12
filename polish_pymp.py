func_map = {"+": lambda a, b: a + b,
            "*": lambda a, b: a * b}
func_keys = list(func_map.keys())


def parse(tokens):
    """ Recursively parses polish notation"""

    if tokens[0] not in func_keys:
        raise ValueError("Tokens not in polish notation")

    arg_count = func_map[tokens[0]].__code__.co_argcount
    args = [parse(tokens[arg_n+1:]) if type(tokens[arg_n + 1]) != int else tokens[arg_n + 1] for arg_n in range(arg_count)]

    return func_map[tokens[0]](*args)


def lex(string):
    return [int(x) if x.isdigit() else x for x in list(string)]

l = "+2*42"
print(parse(lex(l)))