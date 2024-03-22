# 연습문제 25번 - 합집합, 교집합, 차집합을 구현해라. (개인과제)

set1 = set([0, 1, 2, 3, 4, 5])
set2 = set([1, 2, 3])

seti = set1 & set2      # 교집합 입력
setp = set1 | set2       # 합집합 입력
setm = set1 - set2       # 차집합 입력

print(f"합집합: {setp}\n교집합: {seti}\n차집합: {setm}")