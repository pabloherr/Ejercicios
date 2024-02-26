def anagrama(p1:str,p2:str)->bool:
    if len(p1) != len(p2):
        return False
    for i in range(len(p1)):
        for j in range(len(p2)):
            if not p1[i] == p2[j]:
                return False
    return True

anagrama("hola","aloh") # True
anagrama("hola","aloha") # False