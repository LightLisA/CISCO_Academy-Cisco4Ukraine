""" Scenario
  The previous code needs to be improved. It's okay, but it has to be better.
  Your task is to make some amendments, which generate the following results:
   ** the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented
     first)
    ** the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (
      it should be concatenated to the original name)
"""

# C:\Users\Aleksey\Desktop\text.txt
# C:\Users\olly1215\Desktop\text.txt

from os import strerror

# srcname = input("Enter the source file name: ")
srcname = 'C:\\Users\\olly1215\\Desktop\\text.txt'
try:
    src = open(srcname, 'rt', encoding='utf-8')  # відкриваю файл; rt - читаю текст;
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)

dictionary_with_num = {}  # створюю пустий словник

try:
    readin = src.read()  # читаю файл
    for key in readin:
        cnt = 0  # створюю сщотчик
        lowKey = key.lower()  # перевожу все в нижній регістр
        if lowKey in dictionary_with_num:
            continue  # якщо запис уже є в словнику. то скіпаю його
        else:
            if lowKey.isalpha():  # якщо символ є буквою, то ...
                for chart in readin:
                    lowChart = chart.lower()
                    if lowKey == lowChart:  # порівнюю перше значення із файлу, з усіма символами у файлі
                        cnt += 1
                dictionary_with_num[lowKey] = cnt  # записую в словник
            else:
                continue
    src.close()
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)

#   СОРТІРОВКА ПО ЗБІЛЬШЕНЮ ЗНАЧЕННЯ
'''sorted_values = sorted(dictionary_with_num.values())
sorted_dict = {}


for i in sorted_values:
    for k in dictionary_with_num.keys():
        if dictionary_with_num[k] == i:
            sorted_dict[k] = dictionary_with_num[k]'''

# СОРТІРОВКА ПО ЗМЕНШЕНЮ ЗНАЧЕННЯ : reverse=True
sorted_dict = {k: v for k, v in sorted(
    dictionary_with_num.items(), key=lambda element: element[1], reverse=True)}

for i in sorted_dict:  # вивожу словник на екран
    print(str(i) + " --> " + str(sorted_dict[i]))

# outfile = input("Enter the destination file name: ")      # указуємо шлях і ім'я файлу куди записати
outfile = 'C:\\Users\\olly1215\\Desktop\\text.hist'  # записую в файл
try:
    dst = open(outfile, 'wt', encoding='utf-8')
    for i in sorted_dict:
        st = str(i) + " --> " + str(sorted_dict[i]) + "\n"  # створив строку яку буду записувати в файл
        for ch in st:
            dst.write(ch)
    dst.close()  # закриваю сесію - ОБОВ'ЯЗКОВО
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)

src.close()  # закриваю сесію - ОБОВ'ЯЗКОВО
