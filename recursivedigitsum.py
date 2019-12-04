def super_sum(n, k):
    digits = sum(map(int, list(n)))
    if k == 1:
        return digit_sum(digits)
    return digit_sum(digits * k)
    
def digit_sum(digits):
    if digits < 10:
        return digits
    else:
        return digit_sum(sum(map(int, list(str(digits)))))

def superDigit(n, k):
    return super_sum(str(n), k)
    
print(superDigit(148, 3))
print(superDigit(9875, 4))
print(superDigit(123, 3))
print(superDigit(4757362, 10000))

