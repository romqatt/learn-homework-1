"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    answer = input('Как дела?\n')
    while not answer == 'Хорошо':
        try:
            answer = input('Как дела?\n')
        except KeyboardInterrupt:
            return 'Bye'
            break
    return answer
    
if __name__ == "__main__":
    print(hello_user())