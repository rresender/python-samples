

#Naive
# def minTime(machines, goal):
#     days = 1
#     production = 0
#     while True:
#         for m in machines:
#             if days % m == 0:
#                 production+=1
#             if production == goal:
#                 return days
#         days += 1
#     return days

def binarySearch(arr, min, max, goal): 

    while min <= max: 
  
        mid = min + (max - min) // 2; 
          
        if arr[mid] == goal: 
            return mid 
  
        elif arr[mid] < goal: 
            min = mid + 1
        else: 
            max = mid - 1
    return -1


# def minTime(machines, goal):
#     n = len(machines)
#     rate = round(goal / n)
#     minday = rate * min(machines)
#     maxday = rate * max(machines)
#     while minday < maxday:
#         day = (maxday + minday) // 2
#         if sum(day // m for m in machines) >= goal:
#             maxday = day
#         else:
#             minday = day + 1
#     return minday	
    

def minTime(machines, goal):
    n = len(machines)
    minday = round(goal / n) * min(machines)
    maxday = round(goal / n * max(machines))
    while minday < maxday:
        day = (maxday + minday) // 2
        if sum(day // m for m in machines) >= goal:
            maxday = day
        else:
            minday = day + 1
    return minday	
    
# print(minTime([2, 3, 2], 10))
# print(minTime([2, 3], 5))
# print(minTime([1, 3, 4], 10))
# print(minTime([4, 5, 6], 12))

arr = [ 2, 3, 4, 10, 40 ] 
print(binarySearch(arr, 0, len(arr)-1, 10))
