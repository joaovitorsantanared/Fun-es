def imprimirNome(nome):
    print(f"Olá {nome}")

def contagem(numero):
    for i in range(1,numero+1,1):
        for y in range(0,i):
            print(i, end="")
        print()

def palavras(vogais):
    vogal= ["a","e","i","o","u","A","E","I","O","U"]
    qntvogal= 0

    for i in vogais:
        if i in vogal:
            qntvogal +=1

    print(f"A quantidade de vogais será {qntvogal}")

def produto(alimentos, valorunitario, quantidadeproduto):
    total= quantidadeproduto*valorunitario
    return total


def algarismo(numero):
    if numero > 0:
        print("P")
    elif numero < 0:
        print("N")
    else:
        print("Z")


def funcao(*num):
    soma=0
    for x in range (len(num)):
        soma+=num[x]
    print(soma)

def literatura(letras):
    cont = 0
    for x in range (len(letras)-1,-1,-1):
        print(letras[x],end="")
        if letras[x] not in " ":
            cont +=1
    print(f"\n {cont}")



def numericos(lista):
    novalista=[]
    for x in lista:
        if x not in novalista:
            novalista.append(x)
    print(novalista)
