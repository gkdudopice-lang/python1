# NumPy는 파이썬에서 수치 계산과 과학적 연산을 위한 핵심 라이브러리입니다.
# - 데이터의 언어는 '숫자'와 '행렬'이며 이를 효율적으로 처리하기 위해 NumPy를 사용
# - 빅데이터 환경에서 파이썬 기본 리스트로 반복문(for)을 돌리는 것은 매우 느림
# - 넘파이의 벡터와 연산을 쓰면 수백만 개의 데이터를 순식간에 처리할 수 있슴
# - 대규모 다차원 배열 처리
# - 고속 수학 연산 지원
# - 머신러닝, 딥러닝, 데이터 분석에서 필수적으로 사용 됨

import numpy as np # 일반적으로 np라는 별칭을 부여해 사용 함

# 기본 배열 생성
data = [0, 1, 2, 3, 4, 5]
a1 = np.array(data) # 리스트를 넘파이 배열로 만듬
print(data) # 얘는 리스트
print(a1) # 얘는 배열

data2 = [0, 1, 2, 3, 4.4, 5.14, 6.75] # 하나의 타입으로 통일 됨
a2 = np.array(data2)
print(a2)

# 문자열, 실수, 정수를 포함하는 배열을 만들어서 출력 결과 확인 해보기
data3 = ['안녕', '1', 1, 1.1, 2.3, 4]
a3 = np.array(data3)
print(a3)

# 속성 확인
x = np.array([0.1, 0.2, 0.3])
print(x)
print(x.shape) # 배열의 형태를 나타냄
print(x.dtype) # 요소의 데이터 타입 반환

# 특정 범위의 배열 생성
a4 = np.arange(0, 10, 2) # 0에서 10 미만 간격 2로
print(a4)

# 1 ~ 100까지, 간격은 3
a5 = np.arange(1, 100, 3)
print(a5)

# 0 ~ 50 미만, 간격은 5
a6 = np.arange(0, 50, 5)
print(a6)

# 2차원 배열 생성
a7 = np.arange(12).reshape(4, 3)
print(a7)
print(a7.shape)

# 동일한 간격으로 데이터 생성
a8 = np.linspace(1, 10, 11)
print(a8)

# NumPy 기초 실습
# 1. 리스트 [10, 20, 30, 40, 50]을 NumPy 배열로 만들어 arr1에 저장하고,
# 배열과 type(arr1)을 출력하세요
b = [10, 20, 30, 40, 50]
arr1 = np.array(b)
print(type(arr1))

# 2. np.array([True, 1, 2])의 출력 결과와 dtype은 무엇일까요?
b1 = np.array([True, 1, 2])
print(b1)
print(b1.dtype)

# 3. 2행 3배열 [[1,2,3], [4,5,6]]을 만들고 shape와 dtype을 출력하세요
# b2 = np.arange(1,7,1).reshape(2, 3)
b2 = np.array([[1,2,3], [4,5,6]])
print(b2.dtype)
print(b2.shape)

# 4. np.arange()를 사용해 2부터 20까지(20포함) 짝수 배열을 만드세요
b3 = np.arange(2, 21, 2)
print(b3)

# 5. np.arange()를 사용해 [10 9 8 7 6 5 4 3 2 1]을 만드세요
b4 = np.arange(10, 0, -1)
print(b4)

# 6. np.arange()로 0 부터 1 미만까지의 0.1 간격의 배열을 만들고,
# 요소가 몇 개인지 출력 결과로 확인하세요
b5 = np.arange(0, 1, 0.1)
print(len(b5))

# 특정 숫자로 채워진 배열
b6 = np.zeros(10)
print(b6)
b7 = np.zeros((3, 4))
print(b7)

b8 = np.ones(10)
print(b8)

b9 = np.eye(4) # 4x4
print(b9)

# 배열의 데이터 타입 변환
b10 = np.array(['1.5', '0.62', '2', '3.14', '3.141592'])
print(b10)
print(b10.dtype) #<U8의 의미는 데이터 형식이 유니코드이며 문자의 수는 최대 8개라는 의미

num_b10 = b10.astype(float) #문자열을 실수 타입으로 변환
print(num_b10)

b11 = np.array(['1', '2', '3', '4', '7', '9'])
num_b11 = b11.astype(int) #문자열을 정수 타입으로 변환
print(num_b11)

# 난수 배열의 생성
# rand() : 0~1미만의 실수로 난수 배열을 생성
b12 = np.random.rand(2,3)
print(b12)
b13 = np.random.rand(2,3,4)
print(b13)

# randint() : 지정된 범위에 해당하는 정수로 난수 배열을 생성
b14 = np.random.randint(10, size=(5,4)) # 0~9 사이의 난수를 5행 4열로 생성
print(b14)

# 실습 문제2
# 1. 0으로 채워진 요소 5개짜리 1차원 배열을 만들고, 배열과 dtype을 출력하세요.
b15 = np.zeros(5)
print(b15)
print(b15.dtype)

# 2. 0으로 채워진 3행 5열 배열을 만들고 shape를 출력하세요
b16 = np.zeros((3,5))
print(b16)
print(b16.shape)

# 3. 1로 채워진 2행 4열 배열을 만든 뒤, astype()을 사용해 정수형으로 반환하여 출력하세요
b17 = np.ones((2,4)).astype(int)
print(b17)

# 4. np.eye()로 5 x 5 배열을 만들어 출력하고, 이런 형태의 행렬을 무엇이라고 부르는지, dtype은 무엇인지 확인하세요
b18 = np.eye(5)
print(b18)
print(b18.dtype)

# 5. 배열 np.array(['10', '20', '30', '40'])의 dtype을 출력한 뒤, 정수형으로 변환하고 변환 후의 dtype도 출려하세요
b19 = np.array(['10', '20', '30', '40'])
print(b19.dtype)
num_b19 = b19.astype(int)
print(num_b19)

# 6. 0 ~ 1 미만의 실수 난수로 4행 3열 배열을 만들고 shape를 출력하세요
b20 = np.random.rand(4,3)
print(b20)
print(b20.shape)

# 7. np.random.randint()를 사용해 주사위를 10번 던진 결과(1~6)을 1차원 배열로 만드세요
b21 = np.random.randint(1,7, size=10)
print(b21)

# 8. 0 ~ 99 사이의 정수 난수 12개를 1차원 배열로 만든 뒤, 다음을 순서대로 수행하세요
b22 = np.random.randint(0,100, size=12)
b22 = b22.reshape(3,4)
b22 = b22.astype(float)
print(b22)
print(b22.shape)
print(b22.dtype)

# 연산과 함수
b23 = np.array([1, 2, 3])
b24 = np.array([4, 5, 6])
print(b23 + b24)
print(b23 * b24)
print(b23 / b24)

b25 = np.array([10, 20, 30, 40, 50])
print(b25 > 20) # true / false 반환

# 통계 연산
b26 = np.arange(10)
print(f'합계: {b26.sum()}, 평균: {b26.mean()}')
print(f'표준편차: {b26.std()}, 분산: {b26.var()}')
print(f'최솟값: {b26.min()}, 최댓값: {b26.max()}')

# 실전예제
# 동전 던지기
coin = np.random.randint(0, 2, size=100)

a = np.sum(coin == 1)
b = np.sum(coin == 0)

a_ratio = a / len(coin) * 100
b_ratio = b / len(coin) * 100

print(f'앞면: {a} 확률: {a_ratio}, 뒷면: {b} 확률: {b_ratio}')

# 배열 생성 및 연산
# 1부터 10까지의 숫자로 이루어진 1차원 배열을 생성하고, 모든 요소에 5를 더한 결과를 출력하세요.
num = np.arange(1, 11)
print(num)
p_num = num + 5
print(p_num)

# 2차원 배열 만들기
# 1부터 9까지의 숫자를 사용하여 3x3 크기의 2차원 배열을 생성하고 출력하세요.
two = np.arange(1, 10).reshape(3,3)
print(two)

# 배열의 통계 연산
# 1부터 20까지의 숫자로 이루어진 배열을 생성하고, 다음을 계산하세요.
# 1.	배열의 합계
# 2.	배열의 평균
# 3.	배열의 최댓값과 최솟값
npm = np.arange(1, 21)
print(f'합계: {npm.sum()}')
print(f'평균: {npm.mean()}')
print(f'최솟값: {npm.min()}')
print(f'최댓값: {npm.max()}')

# 난수 생성 및 필터링
# 0에서 100 사이의 난수를 10개 생성하고, 50 이상인 값을 출력
nan = np.random.randint(0, 101, size=10)
print(nan[nan>=50])








