time_in_seconds = int(input('Введите кол-во секунд: '))

minutes = time_in_seconds // 60
seconds = time_in_seconds % 60
hours = minutes // 60
minutes = minutes % 60

print(f'{hours:02}:{minutes:02}:{seconds:02}')
