# 표준입력이란? 콘솔로 부터 사용자의 입력을 받음
# - 기본적으로 문자열로 반환되며, 다른 데이터형으로 변환하려면 형변환 함수 사용해야 함

# 이름(문자열), 나이(정수), 성별(문자열), 주소(문자열), 평균(실수) 입력 받아 출력 해보기
'''name = input('이름을 입력: ')
age = int(input('나이 입력: ')) #문자열로 입력 받은 나이를 정수로 변환
gender = input('성별 입력(M/F): ').upper() #대문자로 반환
addr = input('주소 입력: ')
# 국어, 영어, 수학 성적을 입력받아, 총점과 평균 구해 출력하기
korea = int(input('국어 성적 입력: '))
english = int(input('영어 성적 입력: '))
math = int(input('수학 성적 입력: '))
total = korea + english + math
avg = total / 3
# 국어, 영어, 수학 한번에 입력받는 방법
score = list(map(int, input('국어 영어 수학: ').split()))
print(f'총점: {sum(score)}')
print(f'평균: {sum(score)/3:.2f}')


print(f'이름: {name}')
print(f'나이: {age}')
print(f"성별: {'남성' if gender == 'M' else '여성'}")
print(f'주소: {addr}')
print(f'총점: {total}')
print(f'평균: {avg}')'''

# 시간을 24제로 예) 23:56:45 입력 받아 12제로 변환해서 11시56분45초 형태로 출력하기
# split(':')
'''hour, minute, sec = input('24시간 시:분:초 >').split(":")
hour = int(hour)
minute = int(minute)
sec = int(sec)
if hour == 12:
    print(f'오후{hour:02}시{minute:02}분{sec:02}초')
elif hour > 12:
    hour -= 12 #hour = hour - 12
    print(f'오후{hour:02}시{minute:02}분{sec:02}초')
else:
    print(f'오전{hour:02}시{minute:02}분{sec:02}초')'''

# '이름과 주소 입력 : '안내 문구로 이름과 주소를 공백으로 구분해서
# 한 번에 입력받고 (split() 활용), 두 값을 각각 출력하세요.
'''name, addr = input('이름과 주소 >').split(' ')
print(f'이름: {name}')
print(f'주소: {addr}')'''

# '시:분:초 : '안내 문구로 '14:5:9' 형태의 시간을 콜론(:) 기준으로
# 입력받아 map(int,...)로 정수 변환환 뒤, 각 자리를 2자리 폭에 0으로 채워서 출력하세요
'''hour, minute, second = map(int, input('시:분:초 입력: ').split(':'))
print(f'시간: {hour:02}:{minute:02}:{second:02}')'''


# '국어 영어 수학 : '안내 문구로 세 과목 점수를 공백 기준으로 한 번에
# 입력받아 (map(int, input().split())) 평균을 구하고,
# 평균이 60점 이상이면 '합격', 아니면 **'불합격'**을 삼항 연산자로 함께 출력하세요.
kor, eng, mat= map(int, input('국어 영어 수학 점수입력:').split(' '))
avg = (kor + eng + mat) / 3
print(f"{'합격' if avg >= 60 else '불합격'}")







