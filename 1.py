palabra1=input("Dame una palabra ")
palabra2=input("Dame una palabra ")


def dic(palabra1):
    
    dic_palabra={}
    
    for caracter in palabra1:
        if caracter not in dic_palabra:
            dic_palabra[caracter]=1
        elif caracter in dic_palabra:
            dic_palabra[caracter]+=1
    return dic_palabra



def comparacion(dic_palabra,dic_palabra2):
        if dic_palabra==dic_palabra2:
            return True
        else:
            return False

dic_palabra=dic(palabra1)
dic_palabra2=dic(palabra2)
bb=comparacion(dic_palabra,dic_palabra2)
    
if bb is True:
    print("Es un anagrama")
else:
    print("No es un anagrama")