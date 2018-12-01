import time

codificado = []
decodificado = []

def Criptografar():
    arquivo = input('arquivo: ')
    chave = input("key: ")
    arq = open(arquivo, 'r').read()
    novo = []

    for t in arq:
        novo.append(ord(t))
    rodadas = 0

    for y in novo:
        codificado.append(y+ord(chave[rodadas]))
        rodadas += 1
        if rodadas == len(chave):
            rodadas = 0
    print(len(codificado))

    saida = open('ads2.txt', 'w')
    saida.write(str(codificado))
    #saida.write(''.join(str(e) for e in decodificado))
    #print(len(codificado), len(url))

saida = []
def Decriptografar():
    arquivo = input('arquivo: ')
    chave = input("key: ")
    arq = open(arquivo, 'r').read()
    lista = arq.split(', ')
    lista[0] = lista[0].replace('[', '')
    lista[-1] = lista[-1].replace(']', '')
    novo = []
    decodificado = []
    
    rodadas = 0
    for y in lista:
        novo.append(int(y)-ord(chave[rodadas]))
        rodadas += 1
        if rodadas == len(chave):
            rodadas = 0

    for t in novo:
        decodificado.append(chr(t))

    saida = open('ads3.txt', 'w')
    decodificado = ''.join(str(e) for e in decodificado)
    saida.write(decodificado)
    saida.close()
    

Decriptografar()
#print(codificado)
#print()
#Decriptografar(codificado, chave)
#decodificado = ''.join(decodificado)
#print(decodificado)
