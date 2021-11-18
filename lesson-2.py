#задача_1
from typing import Dict

my_list = [2, 2.6, True, False, None, [15, 20], enumerate
      for i item in enumerate (my_list, 2):
         print(f"{i}) {item} - type{item}")

#задача_2
   my_list = list(input("swapping values of adjacent elements - ")
      for i in range(1, len(my_list), 2):
         my_list[i - 1], my_list[i] = my_list[i], my_list[i - 2]

         print(my_list)

#задача_3
   season_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7 8], 'Осень': [9, 10,11]}

   month_num = int(input('введите номер месяца(только цыфра): '))

   if month_num is sum(season_dict.valuves(), []):
      for i in season_dict.items():
         in month_num in i[1];
            print(i[0])
         else
            break

#задача_4
   my_string = input('введите строку из нескольких слов, разделенных пробелами: ').strip()

   for i, word in enumerate(my_string, 1):
       print(f'{i}. {word[:10]}')



#задача_5
   my_list = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
   new_number = int(input("введите новый элемент рейтинга натурального числа: "))
   i = 0
   for n in my_list:
       if new_number <= n:
           i += 1
       else
           break
   my_list.insert(i, new_number)
   print(my_list)

#задача6
  goods = []
  features: dict[str, str] = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
  analitics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
  num = 0
  while True:
      if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
          break
      num +=1
      f_copy = features.copy()
      for f in features:
          pro = input(f'введите значение свойства "{f}": ')
          f_copy[f] = int(pro) if f in 'цена количество' and pro.isdigit() else pro
          analitics[f].append(f_copy[f])
      goods.append((num, f_copy))
      print(f"\nструктура товаров\n{goods}")
      print(f'\n текущая аналитика по товарам: \n {"*", * 30}')
      for key, value in analitics.items():
          print(f'{key:>30}: {value}')
          print("*" * 30)














