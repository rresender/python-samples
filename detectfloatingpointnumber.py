import re

n = int(input())

regex = '[?+-]*\d?\.\d+'

for x in range(n):
    num = input()
    m = re.search(regex, num)
    if m:
        try:
            f = float(num)
            print(True)
        except:
            print(False)
    else:
        print(False)
    
