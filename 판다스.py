# 판다스: Pandas는 테이블 형태의 데이터를 쉽게 다룰 수 있도록 설계된 파이썬 데이터 분ㅅㄱ 라이브러리
# - 데이터 전처리, 탐색, 변환 및 시각화 등의 작업에 널리 사용
# - 행과 열의 구조로 구성된 데이터를 직관적으로 다룰 수 있게 해줌
# - Series(1차원), DataFrame(2차원) 구조 지원
# - 다양한 데이터 파일(CSV, Excel, SQL, JSON 등) 불러오기 가능
# - 결측치 처리, 정렬, 그룹화, 필터링, 통계 분석 등 풍부한 기능 제공
# - 시계열 데이터 처리 기능 내장

# Series - 1차원 데이터 구조: 리스트와 유사하지만, 각 데이터에 인덱스(라벨)가 붙음
import pandas as pd
s1 = pd.Series([10,20,30,40,50])
print(s1)

# DataFrame - 2차원 데이터 구조: 여러 개의 Series가 모여 이루어짐. 행과 열로 구성됨
data = {
    '이름': ['민지', '하니', '다니엘'],
    '수학': [95, 85, 75],
    '영어': [90, 85, 94]
}
df = pd.DataFrame(data)
print(df)

# 특정 행 및 열 추출
print(df['수학']) # 열 추출
print(df.loc[0]) # 행 추출
print(df.loc[1, '영어']) # 특정 행의 열 추출

# 새로운 열 및 행 추가
df['과학'] = [93, 89, 87] # 새 열 추가
df.loc[3] = ['혜인', 92, 89, 77]
print(df)

# 기본 연산
print(df['수학'].sum()) #합계
print(df['수학'].mean())
print(df['수학'].max())
print(df['수학'].min())

# 열 추가
df['반'] = [1, 1, 2, 2]
print(df)

print(df.groupby('반')["수학"].mean())

df = pd.read_csv('exam.csv')
print(len(df))

print(df['math'])
f_df = df[df['math'] >= 80]
print(f_df)

print(df['english'].mean())

df.to_csv('f_exam.csv', index=False)

print(df.groupby('nclass')[['english', 'math']].mean())

print(df.groupby('nclass')['math'].agg(['max', 'min']))

datas = {
    '제품': ['사과', '딸기', '수박'],
    '가격': [1800, 1500, 3000],
    '판매량': [24, 38, 13]
}
dt = pd.DataFrame(datas)
print(dt)

print(f"평균 가격 : {dt['가격'].mean()}")
print(f"평균 판매량 : {dt['판매량'].mean()}")


