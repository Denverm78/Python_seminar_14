# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# 📌 Возвращается строка в нижнем регистре.


english_str = "qwertyuiopasdfghjklzxcvbnm "

def convern_str(original_str):
    result_str = ''
    for i in range(0, len(original_str)):
        if original_str[i] in english_str:
            result_str += original_str[i]
    return result_str 

user_str = "AblObh 76Y76 hHfпышпап77р 5dRкыпси"
print(convern_str(user_str.lower()))