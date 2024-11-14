def solution(n, m, x, y, queries):
    answer = 0
    x_min, x_max, y_min, y_max = x, x, y, y

    for i in range(len(queries)-1, -1, -1):
        way, dx = queries[i]

        if way == 0: # 실제: 좌측 이동 / 거꾸로: 우측 이동
            y_max += dx
            if y_max > m-1: # 벽에 부딪힌 경우
                y_max = m-1 # 최대치로 재설정
            if y_min != 0: 
                y_min += dx # 갈 수 있는 지역 축소

        elif way == 1: # 실제: 우측 이동 / 거꾸로: 좌측 이동
            y_min -= dx
            if y_min < 0: # 벽에 부딪힌 경우
                y_min = 0 # 최소치로 재설정
            if y_max != m-1:
                y_max -= dx # 갈 수 있는 지역 축소

        elif way == 2: #실제: 위로 이동 / 거꾸로: 아래로 이동
            x_max += dx
            if x_max > n-1: # 벽에 부딪힌 경우
                x_max = n-1 # 최대치로 재설정
            if x_min != 0: 
                x_min += dx # 갈 수 있는 지역 축소

        else: #실제: 아래 이동 / 거꾸로: 위에 이동
            x_min -= dx
            if x_min < 0:  # 벽에 부딪힌 경우
                x_min = 0 # 최소치로 재설정
            if x_max != n-1: 
                x_max -= dx # 갈 수 있는 지역 축소
                
        if y_min > m-1 or y_max < 0 or x_min > n-1 or x_max < 0 :
            return 0
        else:
            answer = (y_max - y_min + 1) * (x_max - x_min +1)

    return answer