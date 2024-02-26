def contador_de_palabras(texto):
    texto = texto.lower().replace(",","").replace(".","").replace("!","").replace("?","").replace("¡","").replace("¿","")
    dic = {}
    l = texto.split()
    for i in range(len(l)):
        if not l[i] in dic:
            dic[l[i]] = 1
        else:
            dic[l[i]] += 1
    print(dic)
    
contador_de_palabras("Hola hola, chau. hola chau?")