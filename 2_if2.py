"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(reference_string, difference_string):
    if not isinstance(reference_string, str) or not isinstance(difference_string, str):
      return 0
    elif reference_string.lower() == difference_string.lower():
      return 1
    elif len(reference_string) > len(difference_string) and not difference_string == 'learn':
       return 2
    elif difference_string == 'learn':
       return 3

if __name__ == "__main__":
    print(main('One', 1))               # must be 0
    print(main('One', 'One'))           # must be 1
    print(main('Onee', 'One'))          # must be 2
    print(main('Oneeeeee', 'learn'))    # must be 3
    print(main('One', 'Four'))          # must be None