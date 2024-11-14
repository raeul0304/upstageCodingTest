### **문제 설명**

N개의 스티커가 원형으로 연결되어 있습니다. 다음 그림은 N = 8인 경우의 예시입니다.

!https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/d8d3a8b3-606c-4fb6-baf2-3a96cb53d70c/%E1%84%89%E1%85%B3%E1%84%90%E1%85%B5%E1%84%8F%E1%85%A5_hb1jty.jpg

원형으로 연결된 스티커에서 몇 장의 스티커를 뜯어내어 뜯어낸 스티커에 적힌 숫자의 합이 최대가 되도록 하고 싶습니다. 단 스티커 한 장을 뜯어내면 양쪽으로 인접해있는 스티커는 찢어져서 사용할 수 없게 됩니다.

예를 들어 위 그림에서 14가 적힌 스티커를 뜯으면 인접해있는 10, 6이 적힌 스티커는 사용할 수 없습니다. 스티커에 적힌 숫자가 배열 형태로 주어질 때, 스티커를 뜯어내어 얻을 수 있는 숫자의 합의 최댓값을 return 하는 solution 함수를 완성해 주세요. 원형의 스티커 모양을 위해 배열의 첫 번째 원소와 마지막 원소가 서로 연결되어 있다고 간주합니다.

---

### 제한사항

- sticker는 원형으로 연결된 스티커의 각 칸에 적힌 숫자가 순서대로 들어있는 배열로, 길이(N)는 1 이상 100,000 이하입니다.
- sticker의 각 원소는 스티커의 각 칸에 적힌 숫자이며, 각 칸에 적힌 숫자는 1 이상 100 이하의 자연수입니다.
- 원형의 스티커 모양을 위해 sticker 배열의 첫 번째 원소와 마지막 원소가 서로 연결되어있다고 간주합니다.

---

### 풀이

- 문제에서 제시된 스티커 리스트는 원형이라고 가정해야 하므로 하나를 뜯으면 주변을 뜯을 수 없다는 것을 고려한다면 리스트 상 인덱스 0, -1의 값 중 하나를 선택하는 경우로 풀어보기로 하였습니다.

```python
case1 = max_sticker_sum(sticker[:-1])
case2 = max_sticker_sum(sticker[1:])
```

- dynamic programming 알고리즘을 사용하면 첫 선택부터 누적합을 진행할 수 있게 되며 아래와 같이 모두 합을 0으로 초기화 한 이후 길이가 1이면 dp에 해당값을 넣게 되고 길이가 2일 경우 두 값 중 최대값을 dp에 넣게 되고 길이가 2보다 클 경우에는 가운데 값 또는 양 값의 합 중 최대값을 dp에 넣도록 작성하였습니다.

```python
def max_sticker_sum(stickers):
    dp = [0] * len(stickers)
    dp[0] = stickers[0]
    
    if len(stickers) > 1:
        dp[1] = max(stickers[0], stickers[1])
    
        for i in range(2, len(stickers)):
            dp[i] = max(dp[i-1], dp[i-2] + stickers[i])
    
        return dp[-1]
    else:
        return dp[0]
```