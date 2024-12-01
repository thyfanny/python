#código de teste para um trabalho do curso de administração da ufam
#tema: automatizar a forma de pagamento do restaurante universitário da ufam

#estrutura base para pessoa
#pessoa = {'nome_completo': string,
#           'matricula': string,
#           'cargo': int,
#           'saldo': float}

#cargo: 1 = discente(aluno); 2 = docente(professor); 3 = funcionário; 4 = não paga

#banco de dados para testes
bd = [{  'nome_completo': 'Maria Silva',
         'matricula': '2020345',
         'cargo': 1,
         'saldo': 30.0},
        {'nome_completo': 'Carla Souza',
         'matricula': '2015420',
         'cargo': 2,
         'saldo': 50.0},
        {'nome_completo': 'João Roberto',
         'matricula': '12345',
         'cargo': 3,
         'saldo': 50.0
        }]

#valores expostos na ordem numérica referente aos cargos
#horários: 0 = café da manhã, 1 = almoço, 2 = jantar
valores = [
    #café da manhã
    [2.00, 10.0, 10.0],
    #almoço
    [4.00, 14.0, 13.0],
    #jantar
    [3.00, 13.0, 12.0]]

#busca o usuário no banco de daos à partir da matrícula
def encontrar_usuario(bd, matricula):
    for usuario in bd:
        if usuario.get('matricula') == matricula:
            return usuario
    return None

#retorna o valor a ser pago com base no cargo
def valor_pago(pessoa, horario):
    valor = horario[(pessoa['cargo'])-1]
    return valor

#verifica se a pessoa possui saldo o suficiente
def checa_saldo(pessoa, valor):
    if pessoa['saldo'] < valor:
        return False
    return True

#realiza a transação
def transacao(bd, matricula, horario):
    pessoa = encontrar_usuario(bd, matricula)
    valor = valor_pago(pessoa, horario)
    if not checa_saldo(pessoa, valor):
        print("Saldo insuficiente.")
        return False
    valor_saldo = pessoa['saldo'] - horario[pessoa['cargo']-1]
    novo_saldo = {'saldo': valor_saldo}
    pessoa.update(novo_saldo)
    print("Transação realizada com sucesso.")
    return True

def retorno(bd):
    for pessoa in bd:
        print(pessoa)

while True:
    tipo_refeicao = input("1 = café da manhã, 2 = almoço, 3 = jantar\nInsira o tipo de refeição: ") #1 = café da manhã, 2 = almoço, 3 = jantar
    if tipo_refeicao == 'sair': break
    tipo_refeicao = int(tipo_refeicao)
    if tipo_refeicao not in [1, 2, 3]:
        print("Tipo de refeição inválido, insira novamente.")
        continue
    horario = valores[tipo_refeicao-1]
    while True:
        matricula = input()
        if matricula == 'parar': break
        pessoa = encontrar_usuario(bd, matricula)
        if pessoa == None:
            print("Usuário inválido.")
            continue
        transacao(bd, matricula, horario)
        retorno(bd)
