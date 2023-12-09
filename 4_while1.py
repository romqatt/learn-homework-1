"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

def hello_user():
  answer = input('Как дела?\n')
  return answer
    
if __name__ == "__main__":
    while not hello_user() == 'Хорошо':
      hello_user()