def create_phone_number(n):
    numero = '('
    count=1
    for num in n:
        num = str(num)
        numero+=num
        if count == 3:
            numero+= ') '
        if count == 6:
            numero+= '-'
        count+=1
    return numero

num = [1,2,3,4,5,6,7,8,9,0]
print(create_phone_number(num))