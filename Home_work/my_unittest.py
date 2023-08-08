import unittest
from persona import Employer

 
class TestPerson(unittest.TestCase):
    
    empl_2 = Employer("Kirill", "Medvedev", 45, "Tula", 987654)
    
    def test_metod1(self):
        
        self.assertEqual(self.empl_2.full_name(), 'Kirill Medvedev')
        
    def test_metod2(self):
        
        self.assertEqual(self.empl_2.level(), 4)
    
    def test_metod3(self):
        
        self.assertEqual(self.empl_2.get_age(), 45)
    
    def test_metod4(self):
        
        self.assertEqual(self.empl_2.birthday(), 46)
    
    def test_metod5(self): 
        
        self.assertEqual(self.empl_2.user_city(), 'Tula')
    
if __name__ == '__main__':
    
    unittest.main(verbosity=2)