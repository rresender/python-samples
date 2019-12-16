def count_substring(string, sub_string):
    c = 0
    for i in range(0, len(string)):
        ss = string[i:len(sub_string)+i]
        if sub_string == ss:
            c += 1
    return c
    
print(count_substring('ABCDCDC', 'CDC'))
print(count_substring('I am an Indian, by birth', 'Birth'))
print(count_substring('ThIsisCoNfUsInG', 'is'))
