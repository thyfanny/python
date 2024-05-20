#Crie uma função que multiplica todos os argumentos
#não nomeados recebidos
#Retorne o total para uma variável e mostre o valor
#da variável

def Multiplicacao(*args):
    multi = 1
    for num in args:
        multi = multi * num
        print(f'Multiplicação: {multi}')
        print(f'Variável: {num}')
    return 0

Multiplicacao(2, 3, 5)


#Crie uma função que fala se um número é par ou ímpar
#Retorna se o número é par ou ímpar

def ehPar(*args):
    for num in args:
        if num%2 == 0:
            print (f'O número {num} é par.')
        else:
            print(f'O número {num} é ímpar.')
    return 0

ehPar(4, 5, 200, 245)