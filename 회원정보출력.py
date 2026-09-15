#  회원 정보를 입력 받아서 출력 하는 예제 진행
from selectors import SelectSelector
from typing import cast

# - 이름 입력
# - 나이 입력 : 1~199까지ㅣ 입력 받고 잘못된 값이 오면 재입력을 요청한다
# - 성별 입력 : 영문자 (M과 m은 남성) (F와 f는 여성)으로 입력 받고 나머지는 재입력을 요청한다.
# 출력은 남성 여성으로 출력
# - 직업 입력 : 1(학생), 2(회사원), 3(주부), 4(무직)으로 입력 받고 나머지는 재입력을 요청한다.
# 출력은 직업 이름으로
# - 결과는 마지막에 한번에 출력한다.

# name = input('이름 입력: ')
# while True:
#     age = int(input('나이 입력: '))
#     if 1 <= age <= 199:
#         break
#     else:
#         print('재입력')
#     print()
#
# while True:
#     gender = input('성별 입력(M/F): ').upper()
#     if gender == 'M':
#         gender_str = '남성'
#         break
#     elif gender == 'F':
#         gender_str = '여성'
#         break
#     else:
#         print('재입력')
#
# while True:
#     job = int(input('직업 숫자 입력(1.학생 2.회사원 3.주부 4.무직): '))
#     if job == 1:
#         job_str = '학생'
#         break
#     elif job == 2:
#         job_str = '회사원'
#         break
#     elif job == 3:
#         job_str = '주부'
#         break
#     elif job == 4:
#         job_str = '무직'
#         break
#     else:
#         print('재입력')
# 이렇게도 가능함
# jobs = ['', '학생', '회사원', '주부', '무직']  # 인덱스 번호를 맞추기 위해 0번에 빈 칸('')을 둠
#
# while True:
#     job = int(input('직업 숫자 입력(1.학생 2.회사원 3.주부 4.무직): '))
#
#     # 1부터 4 사이의 숫자인지 한 번에 검사
#     if 1 <= job <= 4:
#         job_str = jobs[job]  # 입력한 숫자에 해당하는 직업 이름을 리스트에서 바로 가져옴
#         break
#     else:
#         print('재입력')

# print(name)
# print(age)
# print(gender_str)
# print(job_str)

# 짝수/홀수 개수 세기
# 정수를 하나씩 계속 입력받다가, -1이 입력되면 반복을 종료합니다.
# 그동안 입력받은 숫자 중 짝수의 개수와 홀수의 개수를 각각 출력하세요
# while과 break 사용
even_count = 0
odd_count = 0
while True:

    num = int(input('정수 입력: '))

    if num == -1:
        break
    elif num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f'짝수: {even_count}, 홀수: {odd_count}')


# 구구단 중 특정 단만 출력하기
# 2~9 사이의 정수를 입력하세요: 3
while True:
    dan = int(input('2~9 사이의 정수를 입력하세요: '))
    if 2 <= dan <= 9:
        break
    print('잘못된 입력')

for i in range(1, 10):
    print(f'{i} * {dan} = {i * dan}')