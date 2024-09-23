#주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오
N =int(input())
num = list(map(int, input().split()))
temp = 0

for i in range(len(num)):
    check = True
    if num[i] == 1:
        check = False
    for j in range(2,num[i]):
        if num[i]%j ==0:
            check = False
            break
    if check == True:
        temp += 1
        
print(temp)        