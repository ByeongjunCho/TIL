def find_max_index(values):
    max_value = 0
    for i in range(len(values) - 1):
        if max_value >= values[i]:
            return i
        elif values[i] < values[i+1]:
            max_value = values[i]
        else:
            return i
    else:
        return i + 1

l1 = [1, 1, 3, 1, 2]  
print(find_max_index(l1))