# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
# 📌 Напишите 3-7 тестов unittest для данного класса.

from rectangle import Rectangle
import unittest

class TestClasseName(unittest.TestCase):
    
    
    def test_metod2(self):
        self.result = pr1.perimeter()
        self.assertEqual(self.result, 24)
    
    def test_metod3(self):
        self.result = pr1.sq()
        self.assertEqual(self.result, 35)
    
    def test_metod4(self):
            self.assertEqual(pr1, pr2)
    
    """def test_metod5(self): 
        result = Rectangle.sub('Hello,Мир789 +World!88Мир')
        self.assertEqual(result, 'hello world')"""
    
if __name__ == '__main__':
    pr1 = Rectangle(5, 7)
    pr2 = Rectangle(7, 5)
    unittest.main(verbosity=2)