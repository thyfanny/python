# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

def Opcoes(questao):
    opc = questao['Opções']
    str = ''
    for op in opc:
        str+= op
        if op == opc[len(opc)-1]:
            str+= '.'
        else:
            str+= ', '
    return str

print("Insira a resposta correta para as seguintes perguntas.")
count = 0
while True:
    if count == len(perguntas): break
    questao = perguntas[count]
    print(f"Pergunta {count+1}: {questao['Pergunta']}")
    print(f'Opções: {Opcoes(questao)}')
    while True:
        resposta = input("Resposta: ")
        if resposta not in questao['Opções']:
            print("Resposta inválida.")
            continue
        elif resposta != questao['Resposta']:
            print("Resposta incorreta :( Tente novamente.")
            continue
        elif resposta == "prox": break
        if resposta == questao['Resposta']:
            if count == len(perguntas)-1:
                print("---------------------------------------\nParabéns! Você conseguiu responder todas as perguntas corretamente.")
                break
            else:
                print("Resposta correta! :) Próxima pergunta.\n---------------------------------------")
                break
    count+=1