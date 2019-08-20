def solution(bridge_length, weight, truck_weights):
    idx = 1 # truck index
    truck = [truck_weights[0]] # truck의 무게
    timer = [0]
    time = 0
    while idx < len(truck_weights):
        if sum(truck) + truck_weights[idx] <= weight:
            truck.append(truck_weights[idx])
            timer.append(0)
            idx += 1
        for i in range(len(timer)):
            timer[i] += 1
        if timer[0] == bridge_length:
            timer.pop(0)
            truck.pop(0)

        time += 1
    return time

print(solution(2, 10, [7,4,5,6]))