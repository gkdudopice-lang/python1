# 리스트 : 연속적으로 저장되는 형태의 자료
# - 크기 지정이 필요 없음
# - 같은 데이터형일 필요가 없음
# - []대괄호로 감싸서 표현, 0개 이상의 원소가 저장 될 수 있음
# - 읽고 쓰기가 가능

# 과목의 수를 알 수 없는 성적을 입력받아, 총점과 평균 구하기
# score = list(map(int, input('성적입력: ').split()))
# print(f'총점: {sum(score)}, 평균: {sum(score) / len(score)}')

mixed = ['안유진', 23, True, [100, 200, 300], ['서울', '대전', '대구', '부산'],{'주소': '경기도'}]
print(mixed)

# 안유진 이름 출력
print(mixed[0])
# 100, 200, 300 출력
print(mixed[3])
# '안유진', 23, True
print(mixed[:3])
# '대전' 출력
print(mixed[-2][1])
# 경기도 출력
print(mixed[-1]['주소'])
# 부산의 '부'만 출력
print(mixed[-2][-1][-2])

members = [
    {
        'neme': '정경수',
        'addr': '경기도 수원시'
    },
    {
        'neme': '아이유',
        'addr': '대전시'
    },
    {
        'neme': '안유진',
        'addr': '인천시'
    },
    {
        'neme': '유인나',
        'addr': '신사동'
    },
    {
        'neme': '장원영',
        'addr': '천안시'
    }
]

print(members[0])

# 요소 추가하기
list_a = [1, 2, 3]
list_a.append(4)
list_a.append(5)
list_a.insert(1, 1000) #시간의 비용이 많이듬
print(list_a)

# 리스트 제거하기
# pop: 인덱스가 없으면 맨 마지막 값 제거, 인덱스 있으면 인덱스 위치의 값 제거, 제거된 값 보여줌
print(list_a.pop(1))
print(list_a.remove(2))
print(list_a)
del list_a[1]
print(list_a)
list_a.clear()
print(list_a)

# 중복제거
my_list = ['A', 'B', 'C', 'D', 'B', 'D', 'E']
new_list = []
for v in my_list:
    if v not in new_list:
        new_list.append(v)
print(new_list)

#집합을 이용한 중복제거가 더 간단/ 순서유지는 안해줌
test_list = {'A', 'B', 'C', 'D', 'B', 'D', 'E'}
print(test_list)

# 10개의 임의의 숫자를 입력 받아 홀수와 짝수 리스트에 나눠 담아서 출력하기
couple = []
single = []
for i in range(10):
    put = int(input('숫자 입력: '))
    if put % 2 == 0:
        couple.append(put)
    else:
        single.append(put)
print(f'짝수: {couple}, 홀수: {single}')
# 위에꺼 극악으로 줄이기
number = list(map(int, input('숫자 입력: ').split()))
odd = list(filter(lambda x: x % 2 == 1, number))
even = list(filter(lambda x: x % 2 == 0, number))

print(f'홀수: {odd}')
print(f'짝수: {even}')





