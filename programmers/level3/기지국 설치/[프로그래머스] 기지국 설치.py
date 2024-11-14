import math

def solution(N, stations, W):
    answer = 0
    current_position = 1
    cover_range = 2*W+1
    
    for station in stations:
        s_index = station - W
        if current_position < s_index:
            uncovered_length = s_index - current_position
            answer += math.ceil(uncovered_length / cover_range)
        
        current_position = station + W + 1
    
    # 마지막 기지국 이후 커버하지 못하는 구역이 있는 경우 처리
    if current_position <= N:
        uncovered_length = N - current_position + 1
        answer += math.ceil(uncovered_length / cover_range)
    
    return answer