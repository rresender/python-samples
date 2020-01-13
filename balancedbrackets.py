def isBalanced(s):
    open_list = ["(" ,"{","["]
    close_list = [")" ,"}","]"]
    stack = []
    for c in s:
        if c in open_list:
            stack.append(c)
        else:
            p = close_list.index(c) 
            n = len(stack)
            if n > 0 and open_list[p] == stack[n-1]: 
                stack.pop()
            else:
                return "NO"
    return "YES" if len(stack) == 0 else "NO"


print(isBalanced("{[()]}"))
print(isBalanced("{[(])}"))
print(isBalanced("{{[[(())]]}}"))

