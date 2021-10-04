def recursion_sum(_list: list):
    if len(_list) == 0:
        return 0
    else:
        return _list.pop() + recursion_sum(_list)


if __name__ == "__main__":
    test_list = [1, 1, 1, 1, 1]
    print(*test_list)
    print("Sum is ", recursion_sum(test_list))
