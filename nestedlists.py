if __name__ == '__main__':
    
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students = sorted(students, key=lambda student: student[1])
    lowest = students[0][1]
    lowests = set()

    for s in students:
        if s[1] > lowest:
            lowest = s[1]
            break

    for s in students:
        if s[1] == lowest:
            lowests.add(s[0])

    lowests = sorted(lowests)

    for n in lowests:
        print(n)


# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39