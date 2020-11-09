# -*- coding: utf-8 -*-


full_base = []
new_base = []

cccccounter = 0
for i in range(250):
    cccccounter += 1
    with open(f'base_2/base_{cccccounter}.txt', 'r', encoding='utf-8') as file:
        try:
            print(f'читаю файл {file}')
            ololo = file.read().split('\n')
            full_base.extend(ololo)
        except Exception as ex:
            print(ex)

print('рочитал все файлы')

print('начинаю сортировать в алфавитном порядке')
full_base.sort()

for item in full_base:
    if item == 'empty_string':
        print('удаляю empty_string')
        full_base.remove(item)
    elif item == ' ':
        print('удаляю пустоту')
        full_base.remove(item)

for item in full_base:
    new_base.append(item+'\n')




print('сортирую еще раз')
new_base.sort()

print('пишем в новую базу')
# for item in full_base:
#     print('*******************порядковый номер******************************')
#     print(full_base.index(item))
with open('base_2/base_result_final.txt', 'a', encoding='utf-8') as file:
    file.writelines(new_base)
