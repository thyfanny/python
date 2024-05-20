"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você  vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

palavra_secreta_normal = "Teclado"
palavra_secreta = palavra_secreta_normal.lower()

count = 0
tentativas = 1
palavra_formada = ''

print("Você deve digitar apenas uma letra por vez, sempre minúscula.")

while True:
    if palavra_formada == palavra_secreta:
        print(f'Parabéns! Após {tentativas} tentativa(s), você descobriu a palavra secreta: {palavra_secreta_normal}.')
        break

    entrada = input().lower()

    if len(entrada) != 1:
        print("Insira uma entrada válida!")
        continue
    
    if entrada == palavra_secreta[count]:
        palavra_formada += entrada
        print(palavra_formada)
        count+=1
        continue
    elif entrada in palavra_secreta:
        palavra_formada += entrada
        print(palavra_formada)
        print("Tente novamente, letra existe em outra posição.")
        palavra_formada = ''
        tentativas += 1
        count = 0
        continue
    else:
        print(palavra_formada+'*')
        print("Tente novamente.")
        palavra_formada = ''
        tentativas += 1
        count = 0
        continue
