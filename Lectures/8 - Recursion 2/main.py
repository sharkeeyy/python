def binary_gen(M:int, prefix = ""):
    if M == 0:
        print(prefix)
        return
    binary_gen(M-1, prefix + "0")
    binary_gen(M-1, prefix + "1")

def every_gen(M:int, N:int, prefix = ""):
    if M == 0:
        print(prefix)
        return
    for i in range(N):
        every_gen(M-1, N, prefix + str(i))

def every_array_gen(M:int, N:int, prefix = None):
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for i in range(N):
        prefix.append(i)
        every_array_gen(M-1, N, prefix)
        prefix.pop()


binary_gen(3)