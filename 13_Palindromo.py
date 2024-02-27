def palindromo(text):
    text = text.lower().replace(" ","").replace(",","").replace(".","").replace("!","").replace("?","").replace("¡","").replace("¿","")
    text_list = text.split()
    inv_list =[]
    for i in range(len(text_list)):
        inv_list.append(text_list[-i])
    if text_list == inv_list:
        print('true')
        return True
    print('false')
    return False

palindromo('Ana lleva al oso la avellana.')