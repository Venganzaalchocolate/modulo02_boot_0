listanumero=[]
strnumero=0

while True and len(listanumero)<5:
    strnumero=(input("Dame un numero "))
    
    if strnumero.isdigit():
        numero=int(strnumero)
        listanumero.append(numero)
        total=sum(listanumero)
        contador=len(listanumero)
        media=total/contador
        print(media)
    
    elif strnumero !='' and strnumero[0] and strnumero [1:].isdigit():
        numero=int(strnumero)
        listanumero.append(numero)
        total=sum(listanumero)
        contador=len(listanumero)
        media=total/contador
        print(media)
    
    else:
        print("el número no es correcto ")