
def super_sum(digits):
    if len(digits) == 1: 
        return int(digits[0])
    return int(digits[0]) + super_sum(digits[1:])

def super_digit(digits):
    if len(digits) == 1: 
       return int(digits[0])
    digits = list(str(super_sum(list(digits))))
    return super_digit(list(digits))

def superDigit(n, k):
    digits = str(n)
    for i in range(k-1):
        digits += str(n)
    return super_digit(list(digits))
    
print(superDigit(148, 3))
print(superDigit(9875, 4))
print(superDigit(123, 3))
print(superDigit(4757362, 10000))

