import re

n = int(input())

regex = '<[a-z][a-z0-9_.-]+@[a-z]+\.[a-z]{1,3}>'

for x in range(n):
    in_put = input()
    if re.search(regex, in_put):
        print(in_put)
