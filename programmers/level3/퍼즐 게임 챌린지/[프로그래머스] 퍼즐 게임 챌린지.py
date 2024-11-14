def time_to_solve(level, diff, time_cur, time_prev):
    if level >= diff:
        return time_cur
    else:
        return (diff - level) * (time_cur + time_prev) + time_cur

def solution(diffs, times, limit):
    left, right = 1, max(diffs)

    while left < right:
        mid = (left + right) // 2
        total = 0

        for i in range(len(diffs)):
            # 처음 위치에만 time_prev가 0
            if not i:
                time_prev = 0
            else:
                time_prev = times[i - 1]

            time_cur = times[i]
            total += time_to_solve(mid, diffs[i], time_cur, time_prev)

        if total <= limit:
            right = mid
        else:
            left = mid + 1

    return left