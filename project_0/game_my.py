"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Угадывание числа меньше чем за 20 попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0 # Счетчик количества попыток
    min = 1 # Начало диапазона
    max = 101 # Конец диапазона
    pridict_number = np.random.randint(min, max) # Загадали число
    
    while True:
        count += 1
     
        middle = (min+max) // 2 # Находим середину диапазона
        
        if middle > pridict_number:
            max = middle
            
        elif middle < pridict_number:
            min = middle
            
        else:
            print(f'Компьютер угадал число {pridict_number} за {count} попыток')
            break
    return count
    
print(f'Количество попыток: {random_predict()}')


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # Список для сохранения количества попыток
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # Загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number)) # Заносим результаты в список

    score = int(np.mean(count_ls)) # Находим среднее количество попыток

    print(f'Алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
score_game(random_predict)