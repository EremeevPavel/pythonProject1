x = int(input("Начало пробежек, в км: "))
y = int(input("Конечная цель: "))
day = 1
print(f'{day}'"-й день пробежек: ", f'{x}')
while x < y:
    x *= 1.1
    day += 1
    q = x
    print(f'{day}'"-й день пробежек: ", f'{q:.2f}')
print(f"Ответ: На {day}-й день цель будет достигнута")
