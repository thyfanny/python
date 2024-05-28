#recebe uma string e gera uma hashtag a partir dela, caso a hashtag possua mais de 140 caracteres,
#ou receba entrada vazia, deve retornar False

def generate_hashtag(s):
    count = 0
    output = '#'
    while True:
        if count == len(s): break
        letra = s[count].lower()
        if letra == ' ':
            count+=1
            continue
        if s[count-1] == " " or count == 0:
            letra = letra.upper()
        output += letra
        count+=1
    if len(output) > 140 or s == '':
        return False
    return output

print(generate_hashtag(""))