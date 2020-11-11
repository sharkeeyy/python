def quick_sort(A:list):
    if len(A) < 2:
        return A
    else:
        pivot = A[0]
        left = [i for i in A[1:] if i <= pivot]
        right = [i for i in A[1:] if i > pivot]
        print("A = ", A)
        print("pivot = ", pivot)
        print("left = ", left)
        print("right = ", right)
        return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    A = [4, 3, 1, 8, 6, 7, 2]
    print(quick_sort(A))
