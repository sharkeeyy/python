list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

func = lambda x: x%2 == 0

print(list(map(func, list1)))
