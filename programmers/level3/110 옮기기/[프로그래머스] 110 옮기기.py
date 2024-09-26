def solution(s):
    answer = []
    mask = ['1', '1', '0']

    for x in s:
        # 모든 '110' 제거
        removed_cnt = 0
        stack = []
        for ch in x:
            stack.append(ch)
            while stack[-3:] == mask:
                for _ in range(3):
                    stack.pop()
                removed_cnt += 1
        remained = ''.join(stack)

        # 완성된 문자열이 최대한 사전 순으로 앞에 오는 위치에 삽입.
        insert_idx = remained.find('111')
        if insert_idx < 0:
            insert_idx = remained.rfind('0') + 1
        final_str = remained[:insert_idx] + '110' * removed_cnt + remained[insert_idx:]

        answer.append(final_str)
    return answer