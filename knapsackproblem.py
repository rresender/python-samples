
def ks(weight, values, n, capacity):
    if n == 0 or capacity == 0:
        return 0
    elif weight[n] > capacity:
        return ks(weight, values, n-1, capacity)
    else:
       t1 =  ks(weight, values, n-1, capacity)
       t2 = values[n] + ks(weight, values, n-1, capacity - weight[n])
       return max(t1, t2)

weights = [1, 2, 4, 2, 5]
values = [5, 3, 5, 3, 2]
c = 10
print(ks(weights, values, len(values)-1, c))    
        