# 10명의 성적에대한 총점, 평균, 최소 점수, 최대 점수 구하는 코드
#
# - 10명의 성적을 입력 받아 총점, 평균, 최소 점수, 최대 점수를 계산하는 코드 작성
# - 점수 입력은 공백 기준으로 연속
# scores = []
# for i in range(10):
#     score = int(input('점수를 입력하세요: '))
#     scores.append(score)
#
# g_total = sum(scores)
# g_avg = (sum(scores) / 3)
# g_min = min(scores)
# g_max = max(scores)
#
# print('10명 전체의 성적 결과')
# print(f'총점: {g_total}')
# print(f'평균: {g_avg}')
# print(f'최소값: {g_min}')
# print(f'최대값: {g_max}')


# - 양의 정수 n을 입력 받아 n * n 크기의 행렬을 출력하는 프로그램 작성
# - 이 때 행렬의 값은 1부터 시작하여 왼쪽에서 오른쪽, 위에서 아래 순서대로 채움
# n = int(input('정수를 입력하세요: '))
#
# for i in range(1, n*n+1):
#     print(f'{i:4}', end = '')
#     if i % n == 0: print()


# 중복 없는 로또 번호 생성하기
# - 1부터 45사이의 6개의 수를 랜덤 함수를 이용해 생성하며 중복값이 발생하지 않도록 함.
# import random
# numbers = []
# while True:
#     number = random.randint(1, 45)
#     if number not in numbers:
#         numbers.append(number)
#     if len(numbers) == 6:
#         break
# print(numbers)


# - 메뉴는 [1]예매하기, [2]종료하기
# - 사용자로부터 좌석번호(index)를 입력받아 예매하는 시스템이다. (좌석은 10개이다.)
# - [V] [V] [V] [  ] [  ] [  ] [  ] [  ] [  ] [  ]
# - 예매가 완료되면 해당 좌석 값을 1로 변경한다.
# - 이미 예매가 완료된 좌석은 재구매할 수 없다.
# - 한 좌석당 예매 가격은 12000원이다.
# - 프로그램 종료 후, 해당 영화관의 총 매출액을 출력한다.
seat = [0] * 10
PRICE = 12000

# 좌석 보여주기
def show_seat():
    for i in seat:
        if i == 0:
            print('[ ]', end='')
        else:
            print('[V]', end='')
    print()
# 예매하기
def select_seat():
# 종료하기












