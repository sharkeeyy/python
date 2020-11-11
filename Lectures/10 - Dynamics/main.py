def fib(n):
    f = [0, 1] + [0]*(n-2)
    for i in range(2, n):
        f[i] = f[i-1] + f[i-2]
    return f

def paths_2(n):
    K = [0, 1] + [0]*(n-2)
    for i in range(2, n):
        K[i] = K[i-1] + K[i-2]
    return K

def paths_logic(n, allowed:list):
    K = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        if allowed[i]:
            K[i] = K[i-1] + K[i-2]
    return K

print(paths_logic(10, [1, 1, 1, 1, 0, 1, 1, 0, 1 ,1, 1]))