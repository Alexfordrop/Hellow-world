number = 43
running = True
while running:
    guess = int(input('Введите целое цисло : '))
    if guess == number:
        print('Поздравляю, вы угадали, ')
        print('(хотя и не выиграли никакого приза!)')
    elif guess < number:
        print('Нет, загаданное число немного больше этого.')
    else:
        print('Нет, загаданное число немного меньше этого.')
else:
    print('цикл while закончен.') 
print('Завершение.')