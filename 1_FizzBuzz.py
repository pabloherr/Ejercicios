def FizzBuzz():
    for i in range (15):
        i=i+1
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 != 0 and i % 5 != 0:
            print(i)
FizzBuzz()