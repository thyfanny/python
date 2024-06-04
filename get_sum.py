#recebe dois números e soma todos os valores entre eles, os números não estão necessariamente em ordem crescente

def get_sum(a,b):
    sum = 0
    if b > a:
        maior = b
        menor = a
    else:
        menor = b
        maior = a
    while True:
        if menor > maior: break
        sum += menor
        menor += 1
    return sum

print(get_sum(7,2))
