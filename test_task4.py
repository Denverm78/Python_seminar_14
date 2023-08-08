# Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import pytest
from task2 import convert_str

def testMetod1():
    assert convert_str('hello world') == 'hello world'

def testMetod2():
    assert convert_str('Hello World') == 'hello world'

def testMetod3():
    assert convert_str('hello, +world!') == 'hello world'

def testMetod4():
    assert convert_str('hello,Привет, world!,Мир') == 'hello world'

def testMetod5():
    assert convert_str('Hello,Мир789 +World!88Мир') == 'hello world'

if __name__ == '__main__':
    pytest.main(['-v'])    