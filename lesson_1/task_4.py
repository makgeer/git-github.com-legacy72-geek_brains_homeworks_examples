number = int(input('Введите чилсо: '))

str_number = str(number)

i = 0
temp = 0
while i != len(str_number):
    if int(str_number[i]) == 9:
        temp = 9
        break
    if int(str_number[i]) > temp:
        temp = int(str_number[i])
    i += 1

print(f'Максимальная цифра в числе {number} - {temp}')
