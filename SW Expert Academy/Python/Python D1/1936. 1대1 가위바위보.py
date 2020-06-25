#A와 B의 값을 입력받는다.
a,b = map(int, input('').split())

# 가위(1) 바위(2) 보(3). [가위>보, 보>바위, 바위>가위] 의 결과가 되게 조건문을 작성한다.

if a == 1:

    if b == 2:
        print('B')

    elif b == 3:
        print('A')

    else:
        print('오류가 발생했습니다.')

elif a == 2:

    if b == 3:
        print('B')
    
    elif b == 1:
        print('A')
    
    else:
        print('오류가 발생했습니다.')

elif a == 3:

    if b == 1:
        print('B')

    elif b == 2:
        print('A')
    
    else:
        print('오류가 발생했습니다.')

else:
    print('다시 입력해주세요')


