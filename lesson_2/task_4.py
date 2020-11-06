words = input('Введите слова через пробел: ').split()

for i, word in enumerate(words):
    print(f'{i}: {word[:10]}')
