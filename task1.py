def degree(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    else:
        return degree(a, b - 1) * a

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

print(f'a ^ b = {degree(a, b)}')
