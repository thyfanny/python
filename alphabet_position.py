#given a string, replace every letter with its position in the alphabet
#if anything in the text isn't a letter, ignore it and don't return it

def posicao(letra):
    letra = letra.lower()
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    if letra not in alfabeto:
        return None
    count = 1
    while count < len(alfabeto):
        if letra == alfabeto[count-1]:
            return count
        count+=1

def alphabet_position(text):
    count = 0
    output = ''
    print(len(text))
    while True:
        if count == len(text): break
        letra = text[count]
        pos = posicao(letra)
        print(letra)
        print(pos)
        if pos == None: 
            count+=1
            continue
        pos = str(pos)
        output += pos
        output += ' '
        count += 1
        print(count)
    return output

text = "Hope to be like you"
print(alphabet_position(text))