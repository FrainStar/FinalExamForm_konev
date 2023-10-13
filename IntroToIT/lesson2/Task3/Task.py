#INTRO TO IT 2nd COURSE
# Задача 3: Четное или нечетное?
# Попробуй определить, является ли введенное число четным или нечетным.
def evenorodd(num):
    return "Четное" if num % 2 == 0 else "Нечетное"
num = 5
print(f"{num} - {evenorodd(num)}")
