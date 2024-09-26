def can_transport_in_time(time, a, b, g, s, w, t):
    total_gold = 0
    total_silver = 0
    total_combined = 0

    for i in range(len(g)):
        max_trips = time // (t[i] * 2)
        if time % (t[i] * 2) >= t[i]:
            max_trips += 1

        gold_delivered = min(g[i], max_trips * w[i])
        silver_delivered = min(s[i], max_trips * w[i])
        combined_delivered = min(g[i] + s[i], max_trips * w[i])

        total_gold += gold_delivered
        total_silver += silver_delivered
        total_combined += combined_delivered

        if total_gold >= a and total_silver >= b and total_combined >= a + b:
            return True

    return total_gold >= a and total_silver >= b and total_combined >= a + b
    
def solution(a, b, g, s, w, t):
    
    left = 0
    right = 10**18
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_transport_in_time(mid,a, b, g, s, w, t):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer
