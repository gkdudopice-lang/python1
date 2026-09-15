# 내장함수: 파이썬에서 기본 제공, import 없이 사용

# ls = [32, 45, 48, 57, 84, 99] #연속된 값을 저장할 때 리스트를 사용
# print(f'리스트 출력: {ls}')
# print(f'합계: {sum(ls)}') #값을 전부 더함
# print(f'평균: {sum(ls)/len(ls)}') #평균 구하기
# print(f'최댓값: {max(ls)}')
# print(f'최소값: {min(ls)}')
# print(f'몫과 나머지: {divmod(11, 5)}')
# print(f'오름차순 정렬: {sorted(ls)}')
# print(f'내림차순 정렬: {sorted(ls, reverse=True)}')

# 이름과 5과목의 성적을 입력 받아 이름, 총점, 평균, 최대값, 최소값 구하기
name = input('이름: ')
grade = list(map(int, input('5과목 성적 입력: ').split()))

print(f'이름: {name}')
print(f'총점: {sum(grade)}')
print(f'평균: {sum(grade)/len(grade)}')
print(f'최대값: {max(grade)}')
print(f'최소값: {min(grade)}')




