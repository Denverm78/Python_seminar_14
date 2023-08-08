# Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть: 
# ○ шестизначный идентификационный номер 
# ○ уровень доступа, вычисляемый как остаток от деления суммы цифр id на семь

import doctest

class Persona:

    def __init__(self, f_name: str, l_name: str, age: int, city: str):
        self.f_name = f_name
        self.l_name = l_name
        self._age = age
        self.city = city

    def birthday(self):
        self._age += 1
        return self._age

    def get_age(self):
        return self._age

    def full_name(self):
        return self.f_name + " " + self.l_name
    
    def user_city(self):
        return self.city


class Employer(Persona):
    """
    >>> empl_1.full_name()
    'Lilia Sorokina'
    >>> empl_1.level()
    4
    >>> empl_1.get_age()
    30
    >>> empl_1.user_city()
    'Moscow'
    >>> empl_1.birthday()
    31
    """
    
    def __init__(self, f_name: str, l_name: str, age: int, city: str, id: int):
        self.id = id
        super().__init__(f_name, l_name, age, city)

    def level(self):
        return sum(int(num) for num in str(self.id)) % 7


if __name__ == '__main__':

    empl_1 = Employer("Lilia", "Sorokina", 30, "Moscow", 512647)
    # empl_2 = Employer("Kirill", "Medvedev", 45, "Tula", 987654)
    doctest.testmod(verbose=True)     