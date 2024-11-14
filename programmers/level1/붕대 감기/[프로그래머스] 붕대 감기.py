def solution(bandage, health, attacks):
    t, x, y = bandage
    current_health = health
    current_time = 0
    success_time = 0  # 연속 성공 시간
    
    for attack_time, damage in attacks:
        while current_time < attack_time - 1:
            current_time += 1
            current_health += x  # 초당 회복량 더하기
            success_time += 1  # 연속 성공 시간 증가

            if success_time == t:
                current_health += y
                success_time = 0  # 추가 회복 후 연속 성공 시간 초기화
            
            if current_health > health:
                current_health = health

        current_time = attack_time
        current_health -= damage
        success_time = 0  # 공격을 받으면 연속 성공 시간 초기화

        # 체력이 0 이하가 되면 사망 처리
        if current_health <= 0:
            return -1

    return current_health