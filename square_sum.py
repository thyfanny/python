def square_sum(numbers):
    sum = 0
    for num in numbers:
        sum += num*num
    return sum

numbers = [1, 2, 2]
print(square_sum(numbers))