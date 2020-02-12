def kfactorial(n,k=1):
    if n == 0 or n == 1:
        return 1
    elif n<=k:
        return n
    else:
        return n * kfactorial(n - k,k)
