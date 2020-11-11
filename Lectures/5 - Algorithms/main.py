A = [1, 2, 3, 4, 5]
B = list(A)

print(A)

for i in range(len(A)//2):
    A[i], A[len(A)-1-i] = A[len(A)-1-i], A[i] 
    
print(A)
