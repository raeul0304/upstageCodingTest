def solution(dirs):
    x, y = 0, 0
    visited = set()
    answer = 0
    
    for move in dirs:
        if move == 'U':
            new_x, new_y = x, y + 1
        elif move == 'D':
            new_x, new_y = x, y - 1
        elif move == 'R':
            new_x, new_y = x + 1, y
        elif move == 'L':
            new_x, new_y = x - 1, y
        else:
            pass
        
        if -5 <= new_x <= 5 and -5 <= new_y <= 5:
            path = ((x, y), (new_x, new_y))
            reverse_path = ((new_x, new_y), (x, y))
            if path not in visited and reverse_path not in visited:
                visited.add(path)
                answer += 1
            
            x, y = new_x, new_y
    
    return answer