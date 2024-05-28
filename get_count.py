#conta vogais na frase

def get_count(sentence):
    sentence = sentence.lower()
    count = 0
    countV = 0
    while True:
        if count == len(sentence): break
        letra = sentence[count]
        vogais = 'aeiou'
        if letra not in vogais:
            count+=1
            continue
        countV += 1
        count+=1
    print(countV)
    return 0

sentence = "Contando as vogais."
get_count(sentence)