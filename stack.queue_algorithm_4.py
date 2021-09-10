import time
start = time.time()  # 시작 시간 저장

def solution(bridge_length, weight, truck_weights):
    bridge_length = [0]*bridge_length
    bridge = []

    while truck_weights != []:
        
        bridge.append(bridge_length.pop(0))
        
        if sum(bridge_length,  truck_weights[0]) <= weight:
            bridge_length.append(truck_weights.pop(0))
        else:
            bridge_length.append(0)

    answer = len(bridge_length)+len(bridge)
    return answer


print(solution(100, 100, [10]*10))
print("나의 풀이 >> time :", time.time() - start)


# -----------------------------------------------

start = time.time()  # 시작 시간 저장

import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()

print("남의 풀이 >> time :", time.time() - start)