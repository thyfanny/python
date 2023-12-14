string = "Só sei que nada sei"
string = string.lower()

count = 0
count_letra = 0
atual = 0
letra_atual = str()

while True:
    if count == len(string): break    
    letra = string[count]

    if letra == letra_atual or letra == " ": 
        count+=1
        continue

    count_letra = string.count(letra)

    if count_letra > atual:
        atual = count_letra
        letra_atual = letra
        count += 1
        continue

    count+=1


print(atual, letra_atual)