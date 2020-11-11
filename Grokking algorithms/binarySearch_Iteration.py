list1 = [1, 2, 3, 4, 5, 6]

def binary_search(list, item):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == item:
            return mid
        elif list[mid] < item:
            left = mid + 1
        else: right = mid - 1
 

print(binary_search(list1, 1))
