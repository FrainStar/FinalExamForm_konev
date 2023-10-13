#INTRO TO IT 2nd COURSE
# Задача 10: Квадраты на улице!
# Создай список, содержащий квадраты чисел от 0 до введенного числа.
def gen_square(num):
    return [x**2 for x in range(num)]
num = 5
print(f"{num} первых квадратов: {gen_square(num)}")
