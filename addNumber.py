def increment(number):
    carry = 0
    for i in range(len(number)-1, -1, -1):
        v = number[i] + 1
        if v >= 10:
            carry = 1
        else:
            carry = 0    
        number[i] = v % 10
        if carry == 0:
            return number
            
    if carry == 1:
        result = [0] * (len(number) + 1)
        result[0] = carry
        return result


data = [9,9,8]
print(data)
print(increment(data))
print('\n')

data = [9,9,9]
print(data)
print(increment(data))
print('\n')


data = [2,4,5]
print(data)
print(increment(data))
print('\n')


data = [2,4,9]
print(data)
print(increment(data))
print('\n')

data = [2,9,9]
print(data)
print(increment(data))
print('\n')
