def armstrong(n:int):
    sum = 0
    temp1 = n
    temp2 = n
    i = 0
    while temp1 > 0:
        i +=1
        temp1 //= 10
    while temp2 > 0:
        digit = temp2 % 10
        sum += digit ** i
        temp2 //= 10
    if n == sum:
        return True
    return False
    
a = armstrong(8208)
print(a)