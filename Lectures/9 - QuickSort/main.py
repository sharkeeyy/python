import random

def merge(A:list, B:list):
    C = []
    i = 0
    j = 0
    while (i < len(A)) and (j < len(B)):
        if A[i] <= B[j] :
            C.append(A[i])
            i += 1
        else :
            C.append(B[j])
            j += 1
    while i < len(A) :
        C.append(A[i])
        i += 1
    while j < len(B) :
        C.append(B[j])
        j += 1
    return C

def quickSort(A:list):
    if len(A) <= 1 :
        return
    middle = len(A)//2
    L = A[:middle]
    R = A[middle:]
    quickSort(L)
    quickSort(R)
    print("Merging " + str(L) + " and " + str(R))
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]
  

A = [0]*10
for i in range(len(A)):
    A[i] = random.randint(0, 20)

print(A)
quickSort(A)
print("result = " + str(A))
