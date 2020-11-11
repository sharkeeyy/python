list1 = [1, 2, 3, 4, 5, 6]

def func(x):
    return x * x

list2 = list(map(func, list1))
print(list2)
