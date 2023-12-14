"""Após seus 31 anos, Phoebe decidiu que precisava de uma forma melhor de organizar sua lista de desejos para cada idade. 
Sabendo que você é um ótimo programador, ela pediu para você escrever um programa que, dado os objetivos do ano e quais ela 
já completou, diga o que ela ainda precisa fazer.

A entrada consiste de é composta por:

Inteiro N (0 <= N < 10), que corresponde a quantidade de coisas que a Phoebe quer fazer.
N strings, uma por linha, na qual cada uma corresponde a uma coisa a ser feita.
Inteiro M (0 <= M < 10), que corresponde a quantidade de coisas que a Phoebe já fez.
M strings, uma por linha, na qual cada uma corresponde a uma coisa já feita.
Conhecendo a Phoebe, sabe-se que ela pode acabar tentando registrar coisas que não estavam na lista, neste caso, o registro é ignorado.

É garantido que nunca haverão objetivos repetidos na lista do que Phoebe quer fazer.

A saída deve seguir o formato, caso Phoebe não consiga atingir todos os objetivos:

Ainda falta(m) K objetivo(s)!

Seguido pelos K objetivos restantes, um por linha, na ordem em que aparecem na entrada.

Caso Phoebe tenha completado todos os objetivos, a seguinte mensagem deve ser impressa:

Smelly Cat, Smelly Cat, what are they feeding you?"""

N = int(input("Quantas coisas deseja fazer: "))

count = 0
desejos = []
while True:
    if count == N: break
    novo_desejo = input("Insira seu desejo: ")
    desejos.append(novo_desejo)
    count+=1

M = int(input("Quantidade de coisas realizadas: "))
completou = N == M

count = 0
while True:
    if count == M: break
    realizado = input("Realizado: ")
    pos = 0
    for desejo in desejos:
        if desejo == realizado:
            desejos.pop(pos)
            N-=1
        pos+=1
    count+=1

if completou:
    print("Smelly Cat, Smelly Cat, what are they feeding you?")
else:
    print(f'Ainda falta(m) {N} objetivo(s)!')
    for desejo in desejos:
        print(desejo)