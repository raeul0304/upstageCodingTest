### **문제 설명**

각 점에 가중치가 부여된 트리가 주어집니다. 당신은 다음 연산을 통하여, 이 트리의 모든 점들의 가중치를 0으로 만들고자 합니다.

- 임의의 연결된 두 점을 골라서 한쪽은 1 증가시키고, 다른 한쪽은 1 감소시킵니다.

하지만, 모든 트리가 위의 행동을 통하여 모든 점들의 가중치를 0으로 만들 수 있는 것은 아닙니다. 당신은 주어진 트리에 대해서 해당 사항이 가능한지 판별하고, 만약 가능하다면 최소한의 행동을 통하여 모든 점들의 가중치를 0으로 만들고자 합니다.

트리의 각 점의 가중치를 의미하는 1차원 정수 배열 `a`와 트리의 간선 정보를 의미하는 `edges`가 매개변수로 주어집니다. 주어진 행동을 통해 트리의 모든 점들의 가중치를 0으로 만드는 것이 불가능하다면 -1을, 가능하다면 최소 몇 번만에 가능한지를 찾아 return 하도록 solution 함수를 완성해주세요. (만약 처음부터 트리의 모든 정점의 가중치가 0이라면, 0을 return 해야 합니다.)

---

### 제한사항

- a의 길이는 2 이상 300,000 이하입니다.
    - a의 모든 수는 각각 -1,000,000 이상 1,000,000 이하입니다.
    - `a[i]`는 i번 정점의 가중치를 의미합니다.
- edges의 행의 개수는 (a의 길이 - 1)입니다.
    - edges의 각 행은 `[u, v]` 2개의 정수로 이루어져 있으며, 이는 u번 정점과 v번 정점이 간선으로 연결되어 있음을 의미합니다.
    - edges가 나타내는 그래프는 항상 트리로 주어집니다.

---

### 풀이

- 문제에 맞게 a라는 변수의 합이 0이 되지 못한다면 바로 반환하여 시간 복잡도를 보완해야 한다.

```python
# 1. 전체 가중치 합계가 0이 아닌 경우 -1 반환
if sum(a) != 0:
    return -1
```

- 예제 그림을 살펴본 결과 그래프 관련 문제임이 확실하므로 양방향 그래프 정의를 하였다.

```python
# 2. 트리 그래프 생성
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
```

- 너비기반 그래프순회 알고리즘인 BFS에서는 아래와 같이 기본 정의가 필요하므로 정의하였다.

```python
total_moves = 0
visited = [False] * n
queue = deque([start])
visited[start] = True
parents = [-1] * n
order = []
```

- 너비기반 그래프순회 알고리즘인 BFS에서는 아래와 같이 queue가 존재할 동안에 popleft로 추출하면서 visited하지 않은 노드는 true로 값을 변화함과 동시에 이웃노드를 queue에 삽입하는 과정을 거치게 된다.

```python
while queue:
		node = queue.popleft()
		order.append(node)
		for neighbor in graph[node]:
		    if not visited[neighbor]:
		        visited[neighbor] = True
		        parents[neighbor] = node
		        queue.append(neighbor)
```

- 아래 코드가 가장 중요한데 부모노드는 자식노드의 a값만큼 더해지고 이 절댓값은 즉 계산횟수로 답을 의미한다.

```python
# 가중치 조정: 자식에서 부모로 전파
for node in reversed(order):
    parent = parents[node]
    if parent != -1:
        a[parent] += a[node]
        total_moves += abs(a[node])
```