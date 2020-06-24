
# 숫자를 입력 받는다

answer = 0
number= int(input())

# 주어진 숫자까지(1부터 number 까지)의 값을 모두 더한다
for i in range(1, number+1, 1):
    answer += i
    
print(answer)
