import collections


def is_digit(string):
    if string in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    return False


def get_tokens(string):
    tokens = []
    i = 0
    while i < len(string) - 1:
        if not is_digit(string[i]):
            tokens.append(string[i])
            i += 1
        elif is_digit(string[i]):
            digit = ''
            while is_digit(string[i]):
                digit += string[i]
                i += 1
            tokens.append(digit)

    return tokens


if __name__ == "__main__":
    str = "5+6*200-(11+60/30)*3="
    print(str)

    print(get_tokens(str))
