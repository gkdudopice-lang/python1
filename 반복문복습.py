# while 문
# for i in range(초기값, 최종값, 증감값)
# for e in sequnce

#while 조건식 or True 들어갈 수 있음 true를 사용하면 break 반드시 사용해줘야함
# n = int(input('정수 입력: '))
# while n > 0: #최종값 거꾸로 작성됐다고 생각하면 됨
#     total += n
#     n -= 1
#
# for i in range(1, n+1):
#     total += i
#
# while True:
#     total += n
#     n -= 1
#     if n == 0: break
#
# print(total)

# 입력 받은 숫자의 합 구하기 (리스트)
# map( 함수, 시퀀스형데이터)
square = list(map(lambda a: a**2, [1,2,3,4,5,6,7,8,9,10]))
print(square)

# score = list(map(int, input('정수 입력: ').split()))
# total = 0
# for i in range(0, len(score)):
#     total += score[i]
# for e in score:
#     total += e

# 입력받은 값을 역순으로 출력하기
# for i in range(len(score) -1, -1, -1):
#     print(score[i], end = ' ')

# 별 100개 찍기
for i in range(10):
    print(f'|i={i}|', end='')
    for j in range(10):
        print('*', end = ' ')
    print()

# 입력 : 5
# *
# * *
# * * *
# * * * *
# * * * * *
# n = int(input('입력: '))
# for i in range(n):
#     for j in range(i + 1):
#         print('*', end = ' ')
#     print()

# * * * * *
# * * * *
# * * *
# * *
# *
# n = int(input('입력: '))
# for i in range(n):
#     for j in range(n - i):
#         print('*', end = ' ')
#     print()

# continue : 반복문에서 아래의 문장을 수행하지 않고 반복문으로 이동
n = int(input('정수 입력: '))
# for i in range(n):
#     if i % 2 == 0: continue
#     print(i) # 짝수일 때 위에서 건너 뛰니까 홀수가 출력됨

# contiune 문을 이용해 3과 5의 배수를 제외하고 출력하기
for i in range(n):
    if i % 3 == 0 or i % 5 == 0: continue
    print(i)







