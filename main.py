# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное 
# количество монет, которые нужно перевернуть
import random

first_coin = random.randint(0, 1)
second_coin = random.randint(0, 1)
third_coin = random.randint(0, 1)
fourth_coin = random.randint(0, 1)
fifth_coin = random.randint(0, 1)

print(first_coin, second_coin, third_coin, fourth_coin, fifth_coin)

count_one = 0
count_zero = 0

for i in first_coin, second_coin, third_coin, fourth_coin, fifth_coin:
    if i == 1:
        count_one += 1
    else:
        count_zero += 1
if count_one <= count_zero:
    print(f'минимально перевернуть {count_one}')
else:
    print(f'минимально перевернуть {count_zero}')
