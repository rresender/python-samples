
def caesarCipher(s, k):
    alpha = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    chars = list(s)
    cipher = []
    for c in chars:
        if c in alpha:
            cipher.append(fix(c, k))
        else:
            cipher.append(c)
    return ''.join(cipher)

def fix(c, k):
    for x in range(k):
        i = ord(c)
        if c == 'z':
            c = 'a'
            continue
        elif c == 'Z':
            c = 'A'
            continue
        i += 1 
        c = chr(i)
    return c


print(caesarCipher('abc', 2))
print(caesarCipher('middle-Outz', 2))
print(caesarCipher('Always-Look-on-the-Bright-Side-of-Life', 5))