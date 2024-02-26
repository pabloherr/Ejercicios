def main(str1,str2):
    str1 = str1.lower().replace(",","").replace(".","").replace("!","").replace("?","").replace("¡","").replace("¿","")
    str2 = str2.lower().replace(",","").replace(".","").replace("!","").replace("?","").replace("¡","").replace("¿","")
    l1 = str1.split()
    l2 = str2.split()
    out1 = comparation(l1,l2)
    out2 = comparation(l2,l1)
    print(out1)
    print(out2)

def comparation(l1,l2):
        out = []
        for i in range(len(l1)):
            if not l1[i] in out:
                out.append(l1[i])
            for j in range(len(l2)):
                if l1[i] == l2[j]:
                    out.remove(l1[i])
        return out

main("Hola chau como estas todo bien","hola chau nos vemos mal todo mal")
