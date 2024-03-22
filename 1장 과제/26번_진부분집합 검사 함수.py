# 연습문제 26번 - 25번에 추가로 구현된 집합에서 A가 B의 진부분집합인지 검사하는 함수를 구현해라.

def testset(x, y) :
    if x < y :
        print("A는 B의 진부분집합이다.")
    else :
        print("A는 B의 진부분집합이 아니다.")
set1 = set([0, 1, 2, 3, 4, 5])
set2 = set([1, 2, 3])

seti = set1 & set2      # 교집합 입력
setp = set1 | set2       # 합집합 입력
setm = set1 - set2       # 차집합 입력

print(f"A: {set1}\nB: {set2}")
print(f"합집합: {setp}\n교집합: {seti}\n차집합: {setm}")
testset(set1, set2)