# Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import unittest
from task2 import convert_str

 
class TestClasseName(unittest.TestCase):
    
    def test_metod1(self):
        result = convert_str('hello world')
        self.assertEqual(result, 'hello world')
        
    def test_metod2(self):
        result = convert_str('Hello World')
        self.assertEqual(result, 'hello world')
    
    def test_metod3(self):
        result = convert_str('hello, +world!')
        self.assertEqual(result, 'hello world')
    
    def test_metod4(self):
        result = convert_str('hello,Привет, world!,Мир')
        self.assertEqual(result, 'hello world')
    
    def test_metod5(self): 
        result = convert_str('Hello,Мир789 +World!88Мир')
        self.assertEqual(result, 'hello world')
    
if __name__ == '__main__':
    unittest.main(verbosity=2)



