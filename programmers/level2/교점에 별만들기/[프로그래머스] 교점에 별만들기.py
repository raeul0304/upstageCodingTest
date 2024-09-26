def find_intersection(A1, B1, C1, A2, B2, C2):
    # 두 직선이 평행한지 확인 (A1 * B2 == A2 * B1 이면 평행)
    denominator = A1 * B2 - A2 * B1
    if denominator == 0:
        return None
    
    # 교점 좌표 계산
    x_numerator = B1 * C2 - B2 * C1
    y_numerator = A2 * C1 - A1 * C2
    
    if x_numerator % denominator != 0 or y_numerator % denominator != 0:
        return None  # 교점이 정수가 아니면 제외
    
    x = x_numerator // denominator
    y = y_numerator // denominator
    return (x, y)

def solution(line):
    points = []  # 정수 교점을 저장할 리스트
    
    # 모든 직선 쌍에 대해 교점 계산
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            A1, B1, C1 = line[i]
            A2, B2, C2 = line[j]
            intersection = find_intersection(A1, B1, C1, A2, B2, C2)
            if intersection:
                points.append(intersection)
    
    # 교점이 없으면 빈 문자열 반환
    if not points:
        return []
    
    # 교점들 중 x, y의 최대값과 최소값 찾기
    min_x = min(x for x, y in points)
    max_x = max(x for x, y in points)
    min_y = min(y for x, y in points)
    max_y = max(y for x, y in points)
    
    # 그리드 생성
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    grid = [['.'] * width for _ in range(height)]
    
    # 정수 교점들에 대해 좌표 위치를 설정하여 * 표시
    for x, y in points:
        grid[max_y - y][x - min_x] = '*'  # 좌표 변환
    
    # 각 행을 문자열로 변환하여 반환
    return [''.join(row) for row in grid]