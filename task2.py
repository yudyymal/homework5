def num_sum(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return num_sum(a, b - 1) + 1

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

print(f'a + b = {num_sum(a, b)}')
