# 함수(function)는 코드의 특정 블록을 하나의 이름으로 묶어둔 것
# 반복적으로 사용해야 하는 코드나 논리적인 작업을 함수로 정의하면,
# 가독성, 재사용성, 유지보수성을 높일 수 있음
# 함수는 생성 이후 호출을 해야 실행 됨
# def 키워드 사용
# 일반적으로 식별자 뒤에() 소괄호가 있으면 함수

# 함수의 재사용: 매개변수는 존재하고, 반환값이 없음
def name_card(name, addr, phone):
    print(f'주소: {addr}')
    print(f'전화번호: {phone}')
    print(f'이름: {name}')
    print('-'*30)

name_card("안유진", "서울시 강남구 역삼동", "010-1234-5678")
name_card("장원영", "서울시 강남구 삼성동", "010-1234-9999")
name_card("가을", "수원시 권선구 권선동", "010-1234-1111")

# 매개변수 o, 반환값 x
# 1-1 이름(name), 나이(age), 취미(hobby)를 매개변수로 받아서 아래 형식으로 출력하는 함수
# intro_card()를 작성하시오.
def intro_card(name, age, hobby):
    print(f'이름: {name}')
    print(f'나이: {age}')
    print(f'취미: {hobby}')

intro_card('히히이', 24, '책 읽기')

# 1-2 과목명(subject)과 점수(score)를 매개변수로 받아 '수학 점수: 90점'
# 형식으로 출력하는 print_score() 작성하고, 서로 다른 3개 과목으로 호출해보세요.
def print_score(subject, score):
    print(f'{subject} 점수: {score}')

print_score('수학', 90)
print_score('과학', 88)
print_score('영어', 33)

# 매개변수 o, 반환값 o
# 2-1 두 정수를 입력받아 큰 수를 반환하는 함수 get_max(a, b)를 작성하시오(if 문 사용)
def get_max(a, b):
    if a > b:
        return a # 반환값은 return 사용
    else:
        return b
result = get_max(10, 20)
print(f'큰 수 출력: {result}')

# 2-2 원의 반지름을 입력받아 원의 넓이를 반환하는 함수 circle_area(r)를 작성하시오(원주율은 3,14 사용)
def circle_area(r):
    return 3.14 *(r ** 2)

print(circle_area(10))

# 2-3 정수를 입력받아 짝수면 '짝수', 홀수면 '홀수'를 반환하는 함수 check_even_odd(num)를 작성하시오.
def check_even_odd(num):
    if num % 2 == 0:
        return "짝수"
    else:
        return '홀수'

print(check_even_odd(10))
print(check_even_odd(21))

# 기본값 인자: 함수 선언 시 매개 변수에 대한 기본값을 정의
# - 매개변수에 기본값이 정의 되어 있는 경우 함수 호출 시 인자값을 넣지 않으면 기본값으로 호출
# def profile(name, age=0, job='무직', addr='대한민국'): # = 하고 쓰면 값이 안들어왔을 때 대체 해주는거임
#     print(f'이름: {name}')
#     print(f'나이: {age}')
#     print(f'직업: {job}')
#     print(f'주소: {addr}')
#
# profile('이야아', 22, '아이돌', '대전시')
# profile('장원영', 55, '아이돌')
# profile('이서')

# 가변 매게 변수
def profile(name, age, *lang):
    print(f'이름: {name}, 나이: {age}', end=' ')
    for e in lang:
        print(e, end=' ')
    print()

profile('나희도', 18, 'Python', "Jaca", "C", "C++", "React", "Korlin")
profile('조세호', 38, 'Python', "Jaca", )
profile('유재석', 48, 'Python', "Jaca", "C", "C++",)

lang = 'Python', "Jaca", "C", "C++", "React", "Korlin"
# * 붙여준거는 뒤에 애들 전부 묶어서 lang에 넣어주겠다 라는 것


# 실습 문제: 표준 체중 계산기
# 키(cm)와 성별을 입력받아 표준 체중을 계산하는 함수를 작성하시오.
#
# 함수 이름은 std_weight로 하고, 매개변수는 키(h)와 성별(sex) 두 개를 받는다.
# 표준 체중 공식은 다음과 같다.
# 남성: (키(m))² × 22
# 여성: (키(m))² × 21
# 단, 입력받은 키는 cm 단위이므로 함수 내부에서 m 단위로 변환해야 한다. (h / 100)
# 함수는 계산된 표준 체중 값을 반환(return) 해야 한다. (출력 X)
# input()을 이용해 사용자로부터 키(cm)와 성별을 입력받는다.
# 키는 정수로 변환하여 저장 (int(input(...)))
# 성별은 "남성" 또는 "여성" 문자열로 입력받음
# 함수 호출 결과를 아래 형식으로 출력하시오. (소수점 둘째 자리까지)
def std_weight(h, sex):
    change_h = (h / 100) # 미터 단위 환산

    if sex == '남성':
        weight = (change_h **2) * 22
    elif sex == '여성':
        weight = (change_h ** 2) * 21
    else:
        return None
    return weight

height = int(input('키 입력: '))
gender = input('성별 입력(남성 or 여성): ')

result = std_weight(height, gender)

if result is not None:
    print(f'키: {height}cm {gender}의 표준 체중은 {result:.2f}kg 입니다.')
else:
    print('성별을 "남성" 혹은 "여성"으로 올바르게 입력해주세요.')
# 더 간단하게도 할 수 있음
# def std_weight(h, sex):
#     change_h = (h / 100) # 미터 단위 환산
#
#     if sex == '남성':
#         return (change_h **2) * 22
#     else:
#         return (change_h ** 2) * 21
#
# height = int(input('키 입력: '))
# gender = input('성별 입력(남성 or 여성): ')
# result = std_weight(height, gender)
# print(f'키: {height}cm {gender}의 표준 체중은 {result:.2f}kg 입니다.')

# 소수의 합 구해보기
# 소수인지 아닌지 판별하는 함수 만들기
# 2부터 n까지 숫자를 하나씩 꺼내서, 위 도구에 통과시킨 뒤 결과들을 다 더하자
def prime_func(n):
    is_prime = True # 일단 이 숫자 소수라고 가정하고 시작함
    for i in range(2, n): # 2부터 나 자신-1 까지의 숫자로 다 나눠보자
        if n % i == 0: # 만약 나누어 떨어지는게 하나라도 있다면
            is_prime = False  # 소수가 아님으로 거짓으로 바꾼다

    if is_prime: # 값이 여전히 True라면
        return n # 소수니까 이 숫자 그대로 돌려주고,
    else:
        return 0 # 아니라면 더해도 의미 없는 0을 돌려줌

n = int(input('정수 입력: '))
sum = 0 # 합계를 담을 그릇을 0으로 초기화 한다.

for i in range(2, n): # 2부터 n전까지의 숫자들을 하나씩 차례대로 꺼낸다
    sum += prime_func(i)
print(sum)

