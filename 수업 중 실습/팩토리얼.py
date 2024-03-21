# 팩토리얼(재귀함수)
def fectorial(n):
    if n>1:
        return n+fectorial(n-1)
    else:
        return 0
    
x = int(input("수를 입력하세요: "))
print(f"{x}의 팩토리얼: {fectorial(x)}")