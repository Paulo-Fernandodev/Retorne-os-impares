def odd_numbers(arr):
    impares = []
    for number in arr:
        if number % 2 != 0:
            impares.append (number)
    return impares

check = odd_numbers([2, 7, 8, 11, 14, 20, 5])
print (check)