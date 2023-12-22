"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'item_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'item_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'item_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main(phone):
    phone['total_item_sold'] = sum(phone['item_sold'])
    phone['average_item_sold'] = round(phone['total_item_sold'] / len(phone['item_sold']))

    return phone
    
if __name__ == "__main__":
    phones =   [
      {'product': 'iPhone 12', 'item_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
      {'product': 'Xiaomi Mi11', 'item_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
      {'product': 'Samsung Galaxy 21', 'item_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]}
    ]

    total_solds = 0
    average_solds = 0

    for phone in phones:
      phone = main(phone)

      print(f"Суммарное количество продаж для {phone['product']} - {phone['total_item_sold']}")
      print(f"Среднее количество продаж для {phone['product']} - {phone['average_item_sold']}")

      total_solds += phone['total_item_sold']
      average_solds += phone['average_item_sold']

    print(f'Суммарное количество продаж всех товаров {total_solds}')
    print(f'Среднее количество продаж всех товаров {round(average_solds / len(phones))}')