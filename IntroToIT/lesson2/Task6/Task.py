#INTRO TO IT 2nd COURSE
# Задача 6: Гласные в высоте!
# Посчитай количество гласных букв в строке.
def vowel_count(string):
    return sum(i for i in string if string.lower() in "аеёиоуыэюя")
string = "Привет, мир!"
print(f"В '{string}' {vowel_count(string)} гласных")
