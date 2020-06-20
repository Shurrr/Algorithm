#횟수를 입력 받는다

# 주어진 횟수만큼() 의 2의 제곱의 값까지의 과정을 출력한다
# for i in range(#초깃값, #마지막값(포함안함), #건너뛸 숫자):
#     pass

number = int(input())
for i in range(0, number+1, 1):
    print(2 ** i, end=' ')
