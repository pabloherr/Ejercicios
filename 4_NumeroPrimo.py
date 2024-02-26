def NPrimo(n):
    for j in range(2,n):
        if n % j == 0 and n != j:
            return(False)
    print(n)
    return(True)

def NPrimos():
    l = []
    for i in range(100):
        i += 2
        if NPrimo(i):
            l.append(i)
    print(l)

NPrimos() # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]