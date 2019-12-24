def minion_game(string):
    vowels = "AEIOU"
    n = len(string)
    kev = sum(n-i for i in range(n) if string[i] in vowels)
    stu = n*(n + 1)/2 - kev

    if kev == stu:
        print("Draw")
    elif kev > stu:
        print("Kevin", int(kev))
    else:
        print("Stuart", int(stu))

minion_game('BANANA')