def add_digits(num):
    while num >= 10:
        temp = 0
        while int(num) > 0:
            temp += int(num % 10)
            num /= 10
        num = temp
    return num

print(add_digits(54))
# print(add_digits(38))
# print(add_digits(99))
