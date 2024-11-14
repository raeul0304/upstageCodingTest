def skip(start_m, start_s, end_m, end_s, poss_m, poss_s):
    if (start_m * 60 + start_s) <= (poss_m * 60 + poss_s) <= (end_m * 60 + end_s):
        poss_m = end_m
        poss_s = end_s
    return poss_m, poss_s

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_m, video_s = map(int, video_len.split(':'))
    poss_m, poss_s = map(int, pos.split(':'))
    start_m, start_s = map(int, op_start.split(':'))
    end_m, end_s = map(int, op_end.split(':'))
    poss_m, poss_s = skip(start_m, start_s, end_m, end_s, poss_m, poss_s)
    for idx, cmd in enumerate(commands):
        
        if cmd == 'prev':
            if (poss_m * 60 + poss_s) <= 10:
                poss_m = 0
                poss_s = 0
            else:
                if poss_m == 0:
                    poss_s -= 10
                else:
                    if poss_s >= 10:
                        poss_s -= 10
                    else:
                        poss_m -= 1
                        poss_s += 50

        else:
            if (video_m * 60 + video_s) - (poss_m * 60 + poss_s) < 10:
                poss_m = video_m
                poss_s = video_s
            else:
                poss_s += 10
                if poss_s >= 60:
                    poss_m += 1
                    poss_s -= 60
        
        poss_m, poss_s = skip(start_m, start_s, end_m, end_s, poss_m, poss_s)
                    
    answer = f'{poss_m:02}:{poss_s:02}'
        
        
    return answer