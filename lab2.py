import time
import re

try:
    filePath = input('Введите путь к файлу: ') # Получаем путь к файлу.
    with open(filePath, 'r', encoding='utf8') as file: # Открываем файл.
        string1 = '' # Строка до 000.
        string2 = '' # Строка после 000.
        transitionFlag = False # Flag для обнаружения 000.
        print('Результат работы программы:')
        for line in file: # Читаем построчно файл.
            for symbol in line: # Читаем строку посимвольно.
                if (transitionFlag == False): # Если не встречено 000.
                    string1 += symbol # Добавляем символ к строке1.
                    if string1.endswith('000'): # Если строка1 заканчивается на 000.
                        transitionFlag = True # Флаг переводим в True.
                        string1 = string1[0:-3] # Удаляем 000 из строки.
                else: # Если 000 уже были встречены.
                    string2 += symbol # Добавляем символ в строку2.
        words1 = re.sub(r'[^\w\s]', ' ', string1).split() # Разбиваем строку1 на слова.
        words2 = re.sub(r'[^\w\s]', ' ', string2).split() # Разбиваем строку2 на слова.
        for i in range(1, len(words1), 2): # Меняем каждую пару слов.
            temp = words1[i]
            words1[i] = words1[i - 1]
            words1[i - 1] = temp
        for i in range(1, len(words2), 6): # Меняем каждую 3 пару слов.
            temp = words2[i]
            words2[i] = words2[i - 1]
            words2[i - 1] = temp

        punctuationMarks = ['.', ',', '!', '?', ';', ':'] # Массив знаков пунктуации.
        string1 = re.findall(r"[\w']+|[.,!?;:]", string1) # Разбиваем строку1 на слова и знаки пунктуации.
        string2 = re.findall(r"[\w']+|[.,!?;:]", string2) # Разбиваем строку2 на слова и знаки пунктуации.

        result = '' # Строка результат.
        j = 0 # Вспомогательный счетчик.
        for i in range(0, len(string1)): # Пробегаемся по строке1.
            transitionFlag = False # Флаг на знаки пунктуации переводим в False
            for mark in punctuationMarks: # Пробегаемся по массиву знаков пунктуации.
                if (mark == string1[i]): # Если элемент массива/строки1 является символом.
                    transitionFlag = True # Флаг на знаки пунктуации переводим в True
                    break
            if (transitionFlag == False): # Если элемент в строке1 не знак пунктуации.
                result += words1[j] + ' ' # Заполняем результирующий массив из массива words1.
                j += 1
            else:
                result = result[0:-1] # Удаляем в результирующем массиве последний символ -- ' '
                result += string1[i] + ' ' # Добавляем знак пунктуации из строки1 и пробел после него.

        j = 0
        for i in range(0, len(string2)): # Пробегаемся по строке2.
            transitionFlag = False # Флаг на знаки пунктуации переводим в False
            for mark in punctuationMarks: # Пробегаемся по массиву знаков пунктуации.
                if (mark == string2[i]): # Если элемент массива/строки2 является символом.
                    transitionFlag = True # Флаг на знаки пунктуации переводим в True
                    break
            if (transitionFlag == False): # Если элемент в строке2 не знак пунктуации.
                result += words2[j] + ' ' # Заполняем результирующий массив из массива words2.
                j += 1
            else:
                result = result[0:-1] # Удаляем в результирующем массиве последний символ -- ' '
                result += string2[i] + ' ' # Добавляем знак пунктуации из строки2 и пробел после него.

        print(result)
        print('Время работы программы: ' + str(time.process_time()))
except FileNotFoundError:
    print("Файл *.txt не обнаружен.")
    print('Время работы программы: ' + str(time.process_time()))