def exp_equilibrada(exp):
    l_exp = exp.split()
    l_left = []
    l_right = []
    for i in l_exp:
        if i == '{':
            l_left.append(i)
        elif i == '[':
            l_left.append(i)
        elif i == '(':
            l_left.append(i)
    for i in range(len(l_exp)):
        i += 1
        if l_exp[-i] == '}':
            l_right.append('{')
        elif l_exp[-i] == ']':
            l_right.append('[')
        elif l_exp[-i] == ')':
            l_right.append('(')
    if l_left == l_right:
        print("La expresión está equilibrada.")
    else:
        print("La expresión no está equilibrada.")
        
        
exp_equilibrada("{ [ a * ( c + d ) ] - 5 }")
exp_equilibrada("{  a * ( c + d ) ] - 5 }")

