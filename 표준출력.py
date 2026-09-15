
# 정수 출력
print(30)
age = 23
print('나이: ' + str(age))
print(f'나이: {age}') #f-string 방식으로 출력

# 실수 출력
avg = 76.6667
print(f"성적: {avg:.2f}") #소수점 2번째까지

# 문자열 출력
name = '곰돌이사육사'
print(f'이름: {name}')
print('이름: ' + name)

# 리스트 출력 : 파이썬은 기본적으로 배열이 없고 리스트로 연속된 데이터를 관리 함
score = [99, 88, 77]
print(f"성적: {score[0]}")

# 여러 줄 출력
print("""
동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세.
무궁화 삼천리 화려 강산,
대한사람 대한으로 길이 보전하세~~~
""")

# 줄바꿈 문자 확인 : \n 뉴라인 \r 캐리지리턴
print('동해물과 백두산이 마르고 닳도록 하느님이', end='\n')
print('우하사 우리나라 만세')

# 역 슬래시 \t \'
print('apple\tbanana\tkiwi\tgrape')

# 제어문자, escape sequence : \n, \t, \r, \\, \b
print('동해물과\t 백두산이 \n마르고 닳도록 하\b느님이')
print('우하사 우리나라 만\\세')

print('안녕하세요. \'장원영\'님 환영합니다.')
print("딸기\r바나나\r키위")
# r사용 예시
import sys
'''import time

total_time = 100  # 총 실행 시간 100ms
steps = 100
sleep_time = total_time / steps  # 한 단계당 대기 시간

for i in range(1, steps + 1):
    print(f"\r진행률 : {i}% 입니다.", end="", flush=True)  # end=""로 줄바꿈 방지, flush=True로 즉시 출력
    time.sleep(sleep_time)

print()  # 최종 줄 바꿈 '''

print('파이썬')
print('파' + '이' + '썬')
print('파''이''썬')
print('파', '이', '썬')

# end : 문자열을 출력 하고 난 다음의 동작, 기본값이 줄바꿈(\n)
# sep : 문자열 사이에서 콤마를 만나면 동작, 기본값이 스페이스

print('life is shot', end = ' & ')
print('you', 'need', 'python', sep='\n')

# 정렬과 포맷 지정
# < : 왼쪽 정렬
# > : 오른쪽 정렬
# ^ : 중앙 정렬
num1 = 10
num2 = 100
num3 = 1000

print(f'|{num1:<5}|')
print(f'|{num2:5}|') #기본 오른쪽정렬
print(f'|{num3:^6}|')

#소수점 이하 출력
PI = 3.141592
print(f'{PI:.2f}')

# 다양한 출력 스타일
name = '곰돟이'
age = 23
gender = 'm'
job = '개발자'
addr = '충남 천안시'

# 파이썬 스타일 2, 가장 최근에 추가된 방식(f - string), 3.6 이후
# f와 {}로 사용합니다.
print('=====파이썬 스타일2=====')
print(f'이름 : {name}')
print(f'나이 : {age}')
print(f'성별 : {gender}')
print(f'직업 : {job}')
print(f'주소 : {addr}\n')

# 자바 스타일
print('=====자바 스타일=====')
print('이름 : ' + name)
print('나이 : ' + str(age))
print('성별 : ' + gender)
print('직업 : ' + job)
print('주소 : ' + addr)

# 1. n, \t를 사용하여 아래와 같은 형태로 자기소개를 한 줄의 print() 문으로 출력하세요
# 이름:   김민준
# 직업:   백엔드 개발자
print('이름: \t김민준\n직업: \t백엔드 개발자')

# 2. 따옴표 출력하기
#'오늘도 좋은 하루 되세요!'라고 인사했습니다.
print("'오늘도 좋은 하루 되세요!'라고 인사했습니다.")

# 3. \r로 커서 이동 확인하기
# - 사과 바나나 키위를 연속 입려개서 키위만 나오도록 출력 하기
print('사과\r바나나\r키위')

# 4. '010', '1234', '5678' 세 문자열을 sep='-' 옵션을 사용해서 아래와 같이 출력하세요
# 010-1234-5678
print('010', '1234', '5678', sep='-')

# 5. 아래 세 개의 print() 문을 각각 작성하되, end옵션을 이용해 최종적으로 한 줄의 문장이 되도록 만드세요.
# 결과: 파이썬은 재미있다.
print('파이썬', end='')
print('은', end=' ')
print('재미있다.', end=' \n' )

# 6. 두 가지 스타일로 자기소개 출력하기
# 이름(name), 나이(age), 직업(job) 변수를 출력
print(f"이름: {name}")
print(f"나이: {age}")
print(f"직업: {job}\n")

print('이름: ' + name)
print('나이: ' + str(age))
print('직업: ' + job)

# 7. 정렬로 표 만들기
# num1 = 7, num2 = 43, num3 = 365 세 변수를 각각 너비 6칸으로 가운데 정렬 하여 아래와 같이 출력하세요.
num1 = 7
num2 = 43
num3 = 365
print(f'|{num1:^6}|')
print(f'|{num2:^6}|')
print(f'|{num3:^6}|')

# 8. 원의 반지름 r = 5를 이용해 원의 넓이(3.14159 * r * r)을 구한 뒤, 폭 10칸, 오른쪽 정렬 소수점 둘째 자리까지 출력하세요.
# 넓이:       78.54
r = 5
rdnjs = (3.14159 * r * r)
print(f'넓이: {rdnjs:10.2f}')
















