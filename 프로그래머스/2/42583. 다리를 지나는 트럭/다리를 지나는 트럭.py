from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 트럭을 대기열로 만듦
    truck_weights = deque(truck_weights)
    # 다리를 큐로 만듦 (현재 다리 상태: 무게를 저장할 것임)
    bridge = deque([0] * bridge_length)
    # 현재 다리 위의 트럭들의 무게 합
    current_weight = 0
    time = 0
    
    while truck_weights or current_weight > 0:
        # 시간 경과
        time += 1
        # 다리에서 트럭이 나가면 무게를 줄임
        current_weight -= bridge.popleft()
        
        if truck_weights:
            # 트럭이 다리에 올라갈 수 있는지 확인
            if current_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                current_weight += truck
            else:
                # 트럭이 못 올라가면 0을 넣어 자리를 유지
                bridge.append(0)
    
    return time
