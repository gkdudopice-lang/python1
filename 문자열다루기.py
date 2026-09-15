# 문자열 : 문자가 연속으로 존재하는 것, 파이썬은 문자와 문자열을 구분하지 않음 (전부 문자열)
# "", '', """ """, ''' '''
#from 연산자 import birth_year

# 인덱싱과 슬라이싱
# 인덱싱은 인덱스로 원하는 값을 추출
text = '안녕하세요. 파이썬 입니다'
print(text[0]) # 안
print(text[7]) #파 출력
print(text[-1]) #다 출력

print(text[7:11])
print(text[::2]) #처음부터 끝까지 2칸씩 건너뜀, -1넣으면 역순으로 출력
print(text[:6])

# 주민등록번호를 입력 : 010222 - 2222222
from datetime import datetime
current_year = datetime.now().year
# 생년월일을 : 2001년 2월 22일
# 성별 : 남성
# 나이 : 25
# id = input('주민등록 번호를 입력하세요(-포함): ')
# birth_yy = id[0:2]
#
# birth_month = id[2:4]
#
# birth_day = id[4:6]
#
# gender_code = int(id[7])
# if gender_code in [1, 2]:
#     birth_year = 1900 + int(birth_yy)
# else:
#     birth_year = 2000 + int(birth_yy)
#
#
# if gender_code % 2 == 0:
#     gender = '여성'
# else:
#     gender = '남성'
#
# age = (current_year - birth_year) + 1
# print(f'{birth_year}년 {birth_month}월 {birth_day}일')
# print(f'성별: {gender}')
# print(f'나이: {age}')

# 대소문자 바꾸기 : upper()와 lower()
a = 'Hello Python Program..'
print(a.upper())
print(a.lower())

# isupper(), islower()
for e in a:
    if e.isupper():
        print(f'{e.lower()}', end='')
    elif e.islower():
        print(f'{e.upper()}', end='')
    else:
        print(e, end='')
print()

# 문자열 변경 : replace("", "")
input_str = 'Hello Python Program'
new_str = input_str.replace('Python', 'JavaScript')
print(new_str)

# 문자 갯수 세기: count
text = 'banana'
print(text.count('a'))
text1 = 'google kakao naver oracle openAI oole'
print(text1.count('oo'))

# 문자열 길이 : len()
print(len(text1))

# 문자열 찾기 : find()와 rfind(), 그리고, index()
# find(): 찯은 부분 문자열의 첫 번째 인덱스를 반환합니다. 부분 문자열을 찾지 못하면 -1을 반환합니다.
# index(): 찾은 부분 문자열의 첫 번째 인덱스를 반환합니다. 부분 문자열을 찾지 못하면 ValueError예외를 발생시킵니다.
phrase = '가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서'
print(phrase.find('가장'))
print(phrase.rfind('가장')) #뒤에서 부터 찾지만 인덱스는 앞에서 부터

print(phrase.index('포기'))

print(phrase.find('나에게')) #찾는 결과 없으면 -1
# print(input_b.index('나에게')) # 해당 단어가 없으므로 에러가 발생

new_phrase = phrase.replace('가장', '나에게')
print(new_phrase)

# 문자열 양옆의 공백제거
# - strip() : 양쪽 공백 제거
# - lstrip() : 왼쪽 공백 제거
# - rstrip() : 오른쪽 공백 제거

input_a = """
안녕하세요.
문자열 함수를 알아 봅니다.


"""
print(input_a.strip)
