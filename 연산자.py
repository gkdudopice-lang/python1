# 연산자 : 프로그램에서 값을 계산하거나 변수에 대해 연산을 수행하는 기호
# 신술연산자 : 사칙연산, 나머지 연산
'''i = 10
j = 4
print(i + j) # 덧셈 : 14
print(i - j) # 뺄셈 : 6
print(i * j) # 곱셈 : 40
print(i / j) # 나눗셈 : 2.5
print(i // j) #나머지 : 2
print(i % j) # 몫 : 2
print(i ** 4) # 제곱 : 10 * 10 * 10 * 10

# 문자열 연산
text = 'python'
print(text + 'programing') # 문자열 연결
print(text * 3) # 문자열 반복
print("="*10 + '성적정보' + '='*10)


# 대입 연산자
num1 = 10
num1 += 2
print(num1)
num1 -= 2
print(num1)
num1 *= 2
print(num1)
num1 //= 2
print(num1)
num1 %= 2
print(num1)

# 비교 연산자 : 결과가 참과 거짓으로 반환 됨
a = 10
b = 20
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# 논리연산자 : 참과 거짓을 반환
# and / or / not
x = 5
y = 10
print(x > 0 and x > y)
print(x > 0 or x > y)
print(not(x > 0 or x > y))

# 삼항연산자
age = 18
is_adult = '성인' if age > 19 else '미성년'
print(is_adult)

# 윤년 계산하기
# - 연도가 4로 나누어 떨어 진다.
# - 100으로 나누어 떨어지면 연도는 윤년이 아니다.
# - 400으로 나누어 떨어지면 윤년이다.

year = int(input('연도를 입력하세요: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'{year}은 윤년입니다.')
else:
    print(f'{year}은 윤년이 아닙니다.')

# 100의 자리 정수를 입력받아 100의 자리, 10의 자리, 1의 자리 나누어 담아 합을 구하기
# 입력: 789 => 7 + 8 + 9 = 24
num = int(input('3자리 수를 입력하세요'))
a = num // 100 #100으로 나눈 몫을 구함
b = num % 10 // 10
c = num % 10
total = a + b + c
print(total)'''

# 1. 대입연산자 실습
num = 50
num += 20
print(num)
num *= 3
num %= 7
num -= 2

# 2. 논리연산자로 범위 판별 : 조건문 포함
# count = int(input('점수 입력: '))
# if count >= 60 and count < 80:
#     print('보통')
# else:
#     print('보통 아님')

# 3. 비교 연산자와 삼항 연산자 더 큰 값을 max_num 에 저장하고 출력
# a = int(input('a값 입력: '))
# b = int(input('b값 입력: '))
#
# if a == b:
#     print('두 수가 같습니다.')
# else:
#     max_num = a if a > b else b
#     print(max_num)
#
# # 4. 아래와 같은 형태의 출력 반복과 연결 연산자 사용
# print('*' * 10 + '학생명단' + '*' * 10)

# 5. 짝수/홀수 판별과 나이계산
# 2026 - 태어난 연도
# 계산된 나이가 홀수인지 짝수인지 %로 판별
# 삼항 연산자 사용해서 짝수, 홀수 변수에 저장한 뒤 출력
# from datetime import datetime
# birth_year = int(input('태어난 연도 입력: '))
# current_year = datetime.now().year
# age = current_year - birth_year
# rst = '짝수' if age % 2 == 0 else '홀수'
# print(f'당신의 나이는 {age}이며, {rst}입니다.')
#









