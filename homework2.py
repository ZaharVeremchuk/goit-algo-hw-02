from collections import deque
# Необхідно розробити функцію, яка приймає рядок як вхідний параметр,
# додає всі його символи до двосторонньої черги (deque з модуля collections в Python),
# а потім порівнює символи з обох кінців черги, 
# щоб визначити, чи є рядок паліндромом. Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів,
# а також бути нечутливою до регістру та пробілів.
d = deque()


def func(text: str):
    d = deque([x for x in text])
    while True:
        if(d.__len__() == 1):
            print(f"{text} is palindrom")
            break
        right_symbol = d.pop()
        left_symbol = d.popleft()
        if (right_symbol != left_symbol):
            print(f"{text} is not palindrom")
            break

func("texet")
func("apple")


