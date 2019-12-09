import email.utils
import re

n = int(input())

regex = '<[a-z][a-z0-9_.-]+@[a-z]+\.[a-z]{1,3}>'

for x in range(n):
    in_put = input()
    if re.search(regex, email.utils.parseaddr(in_put)):
        print(in_put)
    
import re, sys
[print(e.strip('\n')) for e in sys.stdin if re.search('<[a-z][a-z0-9_.-]+@[a-z]+\.[a-z]{1,3}>', e, re.I)]