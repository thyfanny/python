#Remover de a os valores presentes em b e preservar sua ordem

def array_diff(a, b):
    lista = []
    for num in a:
        if num not in b:
            lista.append(num)
    return lista

a = [1,2,2,3,3,4]
b = [2, 4]
print(array_diff(a, b))