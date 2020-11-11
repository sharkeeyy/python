import random

def insert_Search(A):
    """ Sorting an array A by insert method
    """
    for i in range(1, len(A)):
        k = i
        while (k > 0) and (A[k] < A[k-1]):
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1

    return A

def choise_Search(A):
    """ Sorting an array A by choise method
    """
    for i in range(0, len(A)-1):
        m = i
        for j in range(i, len(A)):
            if A[j] < A[m]:
                m = j
        A[i], A[m] = A[m], A[i]

    return A

def bubble_Search(A):
    """ Sorting an array A by bubble method
    """
    for i in range(len(A)-1):
        for j in range(1, len(A)):
           if A[j] < A[j-1]: 
               A[j], A[j-1] = A[j-1], A[j]

    return A

A = [0]*10
for i in range(len(A)):
    A[i] = random.randint(0,9)

print(A)

B = bubble_Search(A)

print(B)
