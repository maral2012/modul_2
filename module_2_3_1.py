my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    n = my_list[i]
    i += 1
    if n > 0:
        print(n)
    elif n == 0:
        continue
    else:
        break
print("следующее число отрицательное")
