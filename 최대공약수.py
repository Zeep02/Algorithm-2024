#최대 공약수 알고리즘 1: 서로 비교해 가장 큰 수를 출력.
def gcd(a,b):
    for x in a:
        for y in b:
            if x==y:
                max = y
    return max

def divisor(x,listx):
    for i in range(1, x+1):
        if not x % i == 0:
            if i in listx:
                listx.remove(i)

a, b = input("두 수를 입력하세요.").split()
a = int(a)
b = int(b)
lista = []
listb = []
if a < b:
    temp = a
    a = b
    b = temp
for x in range(1, a+1):
    lista.append(x)
for y in range(1, b+1):
    listb.append(y)

divisor(a,lista)
divisor(b,listb)
max = gcd(lista,listb)

print(f"최대 공약수는 {max}입니다. ")