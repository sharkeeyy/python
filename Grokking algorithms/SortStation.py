
def is_digit(string):
    if string in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    return False


def is_sign(string):
    if string in ['(', ')', '+', '-', '/', '*', '=']:
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


def make_operation(digits:list, signs:list):
    y = digits.pop()
    x = digits.pop()
    sign = signs.pop()
    if sign == "+":
        res = x + y
    elif sign == "-":
        res = x - y
    elif sign == "/":
        res = x / y
    elif sign == "*":
        res = x * y
    digits.append(res)


if __name__ == "__main__":
    testString = "1+1+1+1="
    print(testString)

    tokens = get_tokens(testString)
    print(tokens)

    PRIORITY = {'+': 1, '-': 1, '/': 2, '*': 2}
    digits = []
    signs = []
    result = 0

    i = 0
    while i < len(tokens):
        print('Current = ', tokens[i])
        print('Digits = ', digits)
        print('Signs = ', signs)
        print('')
        if not is_sign(tokens[i]):
            digits.append(tokens[i])
            i += 1
        elif (tokens[i] == '+') or (tokens[i] == '-'):
            if len(signs) == 0:
                signs.append(tokens[i])
                i += 1
            elif PRIORITY[tokens[i]] > PRIORITY[signs[len(signs) - 1]]:
                signs.append(tokens[i])
                i += 1
            else:
                make_operation(digits, signs)
        elif tokens[i] == '=':
            make_operation(digits, signs)
            print(digits[0])
            i += 1




