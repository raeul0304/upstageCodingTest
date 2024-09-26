def solution(price, money, count):
    sum_price = 0
    for i in range(0, count+1):
        temp = price*i
        sum_price += temp
    answer = abs(money - sum_price) if money < sum_price else 0

    return answer