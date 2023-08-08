# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import doctest

ENGLISH_STR = 'qwertyuiopasdfghjklzxcvbnm '

def convert_str(original_str):
    """
    >>> convert_str('hello world')
    'hello world'
    >>> convert_str('Hello World')
    'hello world'
    >>> convert_str('hello, +world!')
    'hello world'
    >>> convert_str('hello,Привет, world!,Мир')
    'hello world'
    >>> convert_str('Hello,Мир789 +World!88Мир')
    'hello world'
    """
    original_str = original_str.lower()
    result_str = ''
    for i in range(0, len(original_str)):
        if original_str[i] in ENGLISH_STR:
            result_str += original_str[i]
    return result_str 

if __name__ == '__main__':
    doctest.testmod(verbose=True)