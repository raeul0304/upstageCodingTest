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

def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    
    case1 = max_sticker_sum(sticker[:-1])
    case2 = max_sticker_sum(sticker[1:])
    answer = max(case1, case2)
    
    return answer