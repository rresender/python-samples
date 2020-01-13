def cellCompete(states, days):
    results  = states.copy()
    last = len(states) - 1
    for b in range(days):
        prev = 0
        next = 0
        for i in range(0, last):
            next = states[i+1]
            if prev != next:
                results[i] = 1
            else:
                results[i] = 0
            prev = states[i]
        
        if prev != 0:
            results[last] = 1
        else:
            results[last] = 0
        states = results.copy()

    return results

# print(cellCompete([1, 0, 0, 0, 0, 1, 0, 0], 1))
print(cellCompete([1, 1, 1, 0, 1, 1, 1, 1], 2))

# print(cellCompete([1, 0, 1, 1], 2))
