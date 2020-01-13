def generalizedGCD(num, arr):
    i = 0
    for e in arr:
        i = gcd(e, i)
    return i
   
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

print(generalizedGCD(3, [2, 4]))