# - 사용자로부터 좌석번호(index)를 입력받아 예매하는 시스템이다.
# - 예매가 완료되면 해당 좌석 값을 1로 변경한다.
# - 이미 예매가 완료된 좌석은 재구매할 수 없다.
# - 한 좌석당 예매 가격은 12000원이다.
# - 프로그램 종료 후, 해당 영화관의 총 매출액을 출력한다.

# 좌석 개수 리스트 만들기
seat = [0] * 10 # 0으로 만들어진 리스트 10개 복사
PRICE = 12000 # 변하지 않는 값은 대문자로 작성해줌

# 좌석 출력 함수'
def print_seat():
    for e in seat:
        if e == 0:
            print('[ ]', end=' ')
        else:
            print('[V]', end=' ')
    print()

# 좌석 선택 함수
def choice_seat():
    print_seat() # 기존 좌석 보여주고
    seat_num = int(input('좌석번호 입력: ')) -1 # 인덱스는 0부터라
    if seat[seat_num] == 0: # 아직 예약이 안된 좌석
        seat[seat_num] = 1
        print_seat()
    else:
        print('이미 예약된 좌석 입니다.')

# 좌석 취소하기
def cancel_seat():
    print_seat()
    seat_num = int(input('좌석번호 입력: ')) -1
    if seat[seat_num] == 1:
        seat[seat_num] = 0
        print_seat()
    else:
        print('이미 취소된 좌석입니다.')

# 판매 금액 계산 함수
def total_money():
    cnt = 0
    for e in seat:
        if e == 1:
            cnt += 1
    return PRICE * cnt

# 입력 메뉴 구성
while True:
    print('[1]예매하기')
    print('[2]취소하기')
    print('[3]종료하기')
    sel = int(input('메뉴 선택: '))
    if sel == 1:
        choice_seat()
    elif sel == 2:
        cancel_seat()
    else:
        print(f'총 금액: {total_money()}원')
        break

# 함수로 입력 받은 수가 짝수인지 홀수 인지 결과 출력
def judg_number(n):
    if n % 2 == 0:
        print('짝수')
    else:
        print('홀수')

n = int(input('정수 입력: '))
judg_number(n)

# 입력으로 들어오는 수의 평균을 구해서 반환 후 출력하기
def aver_input(input):
    return sum(input) / len(input)

input = list(map(int, input('정수 입력:').split()))
print(aver_input(input))

# 두번째 수 찾기
def second_num(ls, n):
    cnt = 0  # '내가 찾는 숫자를 몇 번 발견했는지' 세기 위한 카운터 (처음엔 0개)

    for i in range(len(ls)):  # 리스트의 처음부터 끝까지 인덱스(i)를 하나씩 돌면서 확인
        if ls[i] == n:  # 만약 지금 칸의 숫자가 내가 찾는 숫자(n)랑 같다면?!

            if cnt > 0:  # 만약 'cnt가 0보다 크다'는 건 무슨 뜻일까요?
                # 이미 앞에서 한 번 찾았다는 뜻입니다! (즉, 이번이 두 번째 발견)
                return i  # 엇, 드디어 두 번째로 찾았다! 현재 위치(인덱스 i)를 즉시 반환하고 끝냄!

            else:  # 아직 앞에서 찾은 적이 없다면 (이번이 첫 번째 발견이라면)
                cnt += 1  # "자, 첫 번째 발견했어!" 하고 카운터를 1 올려줌

    return -1  # 만약 리스트를 끝까지 다 돌았는데도 두 번째로 등장하지 않았다면 -1 반환

ls = list(map(int, input('리스트 입력: ').split()))
n = int(input('찾는 숫자: '))
print(second_num(ls, n))

# 두 번째로 큰 수 찾기
def second_num(num):
    # 숫자가 2개보다 적으면 두 번째로 큰 수를 구할 수 없으므로 -1 반환
    if len(num) < 2:
        return -1

    # 1. 큰 수부터 내림차순으로 정렬한 결과를 새 변수(sorted_num)에 담기
    sorted_num = sorted(num, reverse=True)

    # 2. 두 번째로 큰 수는 인덱스 1번에 있으므로 반환하기
    return sorted_num[1]


num = list(map(int, input('정수 연속 입력: ').split()))
print(f'두 번째로 큰 수: {second_num(num)}')

# 세자리수 정수 입력받아 가장 큰 수 출력하기
a = b = c = 0
def num_split(input):
    global a, b, c
    a = input // 100
    b = (input % 100) // 10
    c = (input % 100) % 10

def compare_num():
    if a > b:
        if a < c: return a
        else: return c
    else:
        if b > c: return b
        else: return c

n = int(input())
num_split(n)
print(compare_num())