from collections import defaultdict, deque

def solution(a, edges):
    n = len(a)
    # 1. 전체 가중치 합계가 0이 아닌 경우 -1 반환
    if sum(a) != 0:
        return -1
    
    # 2. 트리 그래프 생성
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # 3. BFS를 통해 가중치 조정 횟수 계산
    def bfs(start):
        total_moves = 0
        visited = [False] * n
        queue = deque([start])
        visited[start] = True
        parents = [-1] * n
        order = []
        
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parents[neighbor] = node
                    queue.append(neighbor)
        
        # 가중치 조정: 자식에서 부모로 전파
        for node in reversed(order):
            parent = parents[node]
            if parent != -1:
                a[parent] += a[node]
                total_moves += abs(a[node])
        
        return total_moves
    
    total_moves = bfs(0)  # 시작 노드를 0으로 설정
    
    return total_moves