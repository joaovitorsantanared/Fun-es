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


