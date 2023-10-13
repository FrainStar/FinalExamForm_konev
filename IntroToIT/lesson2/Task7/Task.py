#INTRO TO IT 2nd COURSE
# Задача 7: Факториал на месте!
# Рассчитай факториал введенного числа.
def fact(num):
    return 1 if num == 0 else num * fact(num-1)
num = 5
print(f"Факториал {num} равен {fact(num)}")
