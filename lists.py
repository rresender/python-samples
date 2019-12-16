if __name__ == '__main__':
    
    N = int(input())
    
    results = []

    for n in range(N):
        
        cmd = input()
            
        if "insert" in cmd:
            cmd, i, e = map(str, cmd.split(' '))
            results.insert(int(i),int(e))
            continue

        if "print" in cmd:
            print(results)
            continue

        if "remove" in cmd:
            cmd, e = map(str, cmd.split(' '))
            results.remove(int(e))
            continue

        if "append" in cmd:
            cmd, e = map(str, cmd.split(' '))
            results.append(int(e))
            continue

        if "sort" in cmd:
            results.sort()
            continue

        if "pop" == cmd:
            results.pop()
            continue

        if "reverse" in cmd:
            results.reverse()
            continue
        

# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print