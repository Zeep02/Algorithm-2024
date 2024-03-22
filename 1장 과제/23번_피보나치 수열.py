# 연습문제 23번 - 큐를 이용해 피보나치 수열을 계산하는 프로그램을 작성해라.
# 필요 사항: 스택과 큐의 기능을 사용할 수 있는 deque의 호출, 선입선출 기능 구현을 위한 메소드 사용
from collections import deque
Que = deque()
Que.append(0)
Que.append(1)


for i in range (11) :
    if i>=2 :
        f1 = Que.popleft()  # 리스트의 맨 앞에 해당하는 값을 변수에 저장하고 제거함
        f2 = Que.popleft()
        f = f1 + f2
        Que.appendleft(f2)  # 리스트의 맨 앞에 값을 입력함
        Que.append(f)       # 리스트의 맨 뒤에 값을 입력함
        print(f"F{i}의 값: {f}")
    else :
        print(f"F{i}의 값: {Que[i]}")