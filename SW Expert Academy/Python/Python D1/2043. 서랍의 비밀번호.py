#변수 P(int) 와 K(int)를 선언한다

P, K = map(int,input().split(' '))

#K부터 시작하여 몇번만에 P에 도달하는지 계산한다. answer = P-K+1
#계산한 값을 출력한다.
print(P-K+1)
