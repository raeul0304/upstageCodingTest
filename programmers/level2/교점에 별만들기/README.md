### **문제 설명**

`Ax + By + C = 0`으로 표현할 수 있는 `n`개의 직선이 주어질 때, 이 직선의 교점 중 정수 좌표에 별을 그리려 합니다.

예를 들어, 다음과 같은 직선 5개를

- `2x - y + 4 = 0`
- `2x - y + 4 = 0`
- `y + 1 = 0`
- `5x - 8y - 12 = 0`
- `5x + 8y + 12 = 0`

좌표 평면 위에 그리면 아래 그림과 같습니다.

!https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/d440b8f4-91c3-4272-8a81-876e9aaffb9c/RisingStarGraphBox.jpg

이때, 모든 교점의 좌표는 `(4, 1)`, `(4, -4)`, `(-4, -4)`, `(-4, 1)`, `(0, 4)`, `(1.5, 1.0)`, `(2.1, -0.19)`, `(0, -1.5)`, `(-2.1, -0.19)`, `(-1.5, 1.0)`입니다. 이 중 정수로만 표현되는 좌표는 `(4, 1)`, `(4, -4)`, `(-4, -4)`, `(-4, 1)`, `(0, 4)`입니다.

만약 정수로 표현되는 교점에 별을 그리면 다음과 같습니다.

!https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/15ffe460-62dc-48df-82a2-7d7636809454/RisingStarGraphStar.jpg

위의 그림을 문자열로 나타낼 때, 별이 그려진 부분은 `*`, 빈 공간(격자선이 교차하는 지점)은 `.`으로 표현하면 다음과 같습니다.

`"..........."  
".....*....."  
"..........."  
"..........."  
".*.......*."  
"..........."  
"..........."  
"..........."  
"..........."  
".*.......*."  
"..........."`

이때 격자판은 무한히 넓으니 모든 별을 포함하는 최소한의 크기만 나타내면 됩니다.

따라서 정답은

`"....*...."  
"........."  
"........."  
"*.......*"  
"........."  
"........."  
"........."  
"........."  
"*.......*"`

입니다.

직선 `A, B, C`에 대한 정보가 담긴 배열 `line`이 매개변수로 주어집니다. 이때 모든 별을 포함하는 최소 사각형을 return 하도록 solution 함수를 완성해주세요.

---

### 제한사항

- line의 세로(행) 길이는 2 이상 1,000 이하인 자연수입니다.
    - line의 가로(열) 길이는 3입니다.
    - line의 각 원소는 [A, B, C] 형태입니다.
    - A, B, C는 -100,000 이상 100,000 이하인 정수입니다.
    - 무수히 많은 교점이 생기는 직선 쌍은 주어지지 않습니다.
    - A = 0이면서 B = 0인 경우는 주어지지 않습니다.
- 정답은 1,000 * 1,000 크기 이내에서 표현됩니다.
- 별이 한 개 이상 그려지는 입력만 주어집니다.

---

### 풀이

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/9778e1cb-db33-48e2-b84a-4e8b8723293c/7e5d07ae-b54e-4055-a924-a9f27efd6589/image.png)

- 아래의 함수는 각 line별로 교점을 구하는 로직이고, 우선 평행 여부 및 교점의 소수점 여부를 파악하는 과정을 담고 있다.

```python
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
```

- 아래의 코드는 각 교점의 좌표 중에 최소 최대값을 구하여 그리드 형성에 도움을 받고자 작성하였다.

```python
# 교점들 중 x, y의 최대값과 최소값 찾기
  min_x = min(x for x, y in points)
  max_x = max(x for x, y in points)
  min_y = min(y for x, y in points)
  max_y = max(y for x, y in points)
```