def modulus(n):
    if isinstance(n,int):
        return n % 2
    else:
        return -1


print(modulus(15))