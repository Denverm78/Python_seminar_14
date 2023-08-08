import pytest
from persona import Employer

empl_3 = Employer("Alex", "Korneev", 40, "Voronezh", 555111)

def testMetod1():
    assert empl_3.full_name() == 'Alex Korneev'

def testMetod2():
    assert empl_3.level() == 5

def testMetod3():
    assert empl_3.get_age() == 40

def testMetod4():
    assert empl_3.birthday() == 41

def testMetod5():
    assert empl_3.user_city() == 'Voronezh'


if __name__ == '__main__':
    pytest.main(['-v'])    