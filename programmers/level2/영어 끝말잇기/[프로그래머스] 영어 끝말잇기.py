def solution(n, words):
    answer = [0,0]
    used_words = set()
    prev_word = ""
    
    for i, word in enumerate(words):
        current_word = word
        player = (i % n) + 1
        turn = (i // n) + 1
        
        if len(current_word) < 2:
            answer = [player, turn]
            return answer
        
        if i > 0 and prev_word[-1] != current_word[0]:
            answer = [player, turn]
            return answer
        
        if current_word in used_words:
            answer = [player, turn]
            return answer
        
        used_words.add(current_word)
        prev_word = current_word
    
    return answer