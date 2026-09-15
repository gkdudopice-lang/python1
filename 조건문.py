# 제어문 : 프로그램의 흐름을 제어하는 데 사용
# -조건문 : 입력 값에 따라 특정 코드 블록을 선택적으로 실행 (if문, *(중요) 3항연산자)
# -반복문 : 조건이 충족되는 동안 특정 코드 블록을 반복 실행 (while문, for문)
'''
num = int(input('정수 입력: '))

# 양수 / 음수 구분 하기
if num >= 0:
    print(f'{num}은 양수 입니다.')
else:
    print(f'{num}은 음수 입니다.')

# 홀수 / 짝수 구분하기
if num % 2 == 0:
    print(f'{num}은 짝수 입니다.')
else:
    print(f'{num}은 홀수 입니다.')

# M이면 남성, F면 여성, 그외는 잘 못 입력
gender = input('M/F로 성별을 입력하세요: ').upper() # 소문자로 써도 대문자로 처리
if gender == 'M':
    print('남성')
elif gender == 'F':
    print('여성')
else:
    print('잘못입력')
'''

# 학생의 이름, 국어, 영어, 수학 성적을 입력 받음
# 각각의 성적이 0 ~ 100 사이가 아니면 성적이 잘 못 입력 되었습니다.
# 출력 후 종료
# 성적이 정상 입력 되었다면, 총점과 평균 구하기
# 평균이 90점 이상이면 이름과 등급 A
# 평균이 80점 이상이면 이름과 등급 B
# 평균이 70점 이상이면 이름과 등급 C
# 평균이 60점 이상이면 이름과 등급 D
# 나머지는 이름과 등급 F

name = input('이름 입력: ')
kor, eng, mat = map(int, input('국어 영어 수학 순으로 성적 입력: ').split(' '))


if (kor < 0 or kor > 100) or (eng < 0 or eng > 100) or (mat < 0 or mat > 100):
    print('성적이 잘 못 입력 되었습니다.')
else:

    total = kor + eng + mat
    avg = total / 3

    if avg >= 90:
        print(f'{name}: A')
    elif avg >= 80:
        print(f'{name}: B')
    elif avg >= 70:
        print(f'{name}: C')
    elif avg >= 60:
        print(f'{name}: D')
    else:
        print(f'{name}: F')

    print(f'총점: {total}, 평균: {avg}')

    # 3항연산자 사용한 코드
    # grade = 'A' if avg >= 90 else('B' if avg >= 80 else('C' if avg >= 70 else('D' if avg >= 60 else 'F')))

# 계절을 영문으로 입력 받아 계절에 맞는 문구 출력하기
# spring, summer, fall, autumn, winter 입력 받아서 계절에 맞는 문구 출력
# 단, 비교의 편의를 위해 입력받은 문자열 대문자로 변환해서 비교하기
season = input('4계절 중 하나를 영어로 입력: ').upper()
spring = '봄 봄 봄'
summer = '여 름 여 름'
autumn = fall = '가 을 가 을'
winter = '겨 울 겨 울'
# 여러번 쓰는거 아니면 그냥 변수 안만들고 print에 넣어도 됨

if season == 'SPRING':
    print(spring)
elif season == 'SUMMER':
    print(summer)
elif season == 'AUTUMN' or season == 'FALL':
    print(autumn)
elif season == 'WINTER':
    print(winter)
else:습
    print('작성한 문구를 다시 확인해주세요.')