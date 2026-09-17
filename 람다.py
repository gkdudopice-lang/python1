# 람다: 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현
# 람다 함수를 이용해 익명의 함수를 만들 수 있음
# 람다 함수의 장점은 코드의 간결함, 메모리의 절약

def add(a, b):
    return a + b

print(add(10, 20))

print(f'{(lambda a, b: a + b)(1, 2)}')

def power(n):
    return n*n

out = list(map(lambda x: x*x, [1, 2, 3, 4, 5]))
print(out)

number = list(map(int, input('입력: ').split()))
odd = list(filter(lambda x: x % 2==1, number))
even = list(filter(lambda x: x % 2==0, number))

print(f'홀수: {odd}')
print(f'짝수: {even}')








