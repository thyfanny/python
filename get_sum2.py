#recebe dois números e soma todos os valores entre eles, os números não estão necessariamente em ordem crescente

def get_sum(a,b):
    sum = 0
    maior = max(a,b)
    menor = min(a,b)
    for num in range(menor, maior+1):
        sum += num
    return sum

print(get_sum(7,2))
