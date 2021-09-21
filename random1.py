import random

a = input('Введіть початок: ')
b = input('Введіть кінець: ')


def gen_list(a, b):
    return [i for i in range(int(a), int(b)+1)]


lst = gen_list(a, b)


while True:
    if input("Вибрати число із списка - 1, закінчити роботу програми - 2: ") == "1":
        if len(lst) > 0:
            a = random.choice(lst)
            print(a)
            lst.remove(a)
        else:
            print("Список порожній")
            exit()
    else:
        exit()

