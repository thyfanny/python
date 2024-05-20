#Crie funções que duplicam, triplicam e quadruplicam o parâmetro inserido

def Dobro(num):
    return num*2

def Triplo(num):
    return num*3

def Quadruplo(num):
    return num*4

print('Digite SAIR para encerrar.')
print('Digite D para dobrar, T para triplicar e Q para quadruplicar.')
while True:
    entrada = input("Operação a ser feita: ")
    entrada = entrada.lower()
    if entrada == "sair": break
    num = input("Número: ")
    num = int(num)
    if entrada == 'd':
        print(f'O dobro de {num} é {Dobro(num)}.')
    elif entrada == 't':
        print(f'O triplo de {num} é {Triplo(num)}.')
    elif entrada == 'q':
        print(f'O quádruplo de {num} é {Quadruplo(num)}.')