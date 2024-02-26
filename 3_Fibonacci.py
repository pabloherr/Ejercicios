def fibonacci():
    l = [0,1]

    for i in range(6):
        l.append(l[-1]+l[-2])
    print(l)

fibonacci() # [0, 1, 1, 2, 3, 5, 8]