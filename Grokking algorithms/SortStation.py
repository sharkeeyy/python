import collections


def is_digit(string):
    if string in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    return False


def is_sign(string):
    if string in ['(', ')', '+', '-', '/', '*']:
        return True
    return False


def is_equals(string):
    if string in ['=']:
        return True
    return False


def get_tokens(string):
    tokens = []
    i = 0
    while i <= len(string) - 1:
        if not is_digit(string[i]):
            tokens.append(string[i])
            i += 1
        elif is_digit(string[i]):
            digit = ''
            while is_digit(string[i]):
                digit += string[i]
                i += 1
            tokens.append(int(digit))

    return tokens


if __name__ == "__main__":
    str = "5+6*200-(11+60/30)*3="
    print(str)

    tokens = get_tokens(str)
    print(tokens)

    digits = []
    signs = []
    result = 0

    for token in tokens:
        if not is_sign(token):
            print(token + 'is sign')
        elif token == '+':
            pass
        elif token == '-':
            pass
        elif token == '*':
            pass
        elif token == '/':
            pass
        elif token == '(':
            pass
        elif token == ')':
            pass
        elif token == '=':
            pass



