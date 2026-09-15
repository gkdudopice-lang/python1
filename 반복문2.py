# for 문 : 정해진 범위만큼 반복 수행 할 때 효과적
# for 요소 in 시퀀스:
# for 변수 in range(시작값, 최종값, 증감값):

# ive = ['안유진', '장원영', '이서', '가을', '레이', '리즈']
# for e in ive: #시퀀스형 데이터를 자동으로 반복 수행 하면서 요소의 값을 복사 하면서 수행
#     e += '*'
#     print(e, end=' ')

# for i in range(len(ive)): # 얘는 원본 데이터 바꿔버림...
#     print(ive[i], end=' ')

# for i in range(len(ive) -1, 0 - 1, -1):
#     print(ive[i], end=' ')

# 1~1000 사시의 3의 배수 출력하기
# cnt = 0
# for i in range(1,1000 + 1):
#     if (i % 3) == 0:
#         print(f'{i}', end=' ')
#         cnt += 1
#         if cnt >= 10:
#             print()
#             cnt = 0


# 입력 받은 수의 범위 내의 7의 배수를 출력.
# cnt = 0
# print()
# for i in range(1, 1000+1):
#     if (i % 7) == 0:
#         print(f'{i:5}', end = ' ')
#         cnt += 1
#         if cnt >= 10: # 출력한 개수가 10개가 되면
#             print() # 줄바꿈
#             cnt = 0 # 카운트 초기화
# 한줄에 10개씩 출력
# 정렬{n:5}을 적용해 줄 맞추기

# 입력 받은 문자열을 뒤집어 출력 하기
# 입력: abcdef => fedcba
print()
# st = input('문자열을 입력하세요: ')
# for i in range(len(st) -1, -1, -1):
#     print(st[i], end='')

# 입력 받은 문자열에서 대문자는 소문자로, 소문자는 대문자로 변경해서 출력하기
# strr = input('문자열을 입력하세요: ')
# for ch in strr:
#     if ch.isupper():
#         print(ch.lower(), end ='')
#     elif ch.islower():
#         print(ch.upper(), end ='')
#     else:
#         print(ch, end ='')
# print()

# 정수값을 입력 받아 3의 배수, 5의 배수이면 값을 출력, 10줄에 5개씩 출력
# cnt = 0
# line_cut = 0
# num = int(input('정수값 입력: '))
# for i in range(1, num + 1):
#     if (i % 3 == 0) or (i % 5 == 0):
#         print(f'{i:5}', end=' ')
#         cnt += 1
#         if cnt >= 5:
#             print()
#             cnt = 0
#             line_cut += 1
#
#             if line_cut >= 10:
#                 break

# 이중 for문
# 입력받은 수가 10이라면 10 * 10의 행렬 출력
# cnt = 0
# num = int(input('정수 입력: '))
# for i in range(1, num+1): # 1 ~ num
#     for j in range(1, num+1, 1):
#         cnt += 1
#         print(f'{cnt:4}', end=' ')
#     print()

# 단일 for문으로 변경해서 출력해보기
# 반복문 범위를 num * num
# i % num == 0: print()

# cnt = 0
# num = int(input('정수 입력: '))
# for i in range(1,num*num+1):
#     print(f'{i:4}', end=' ')
#     if i % num == 0:
#         print()

# 2~9단 까지 구구단 출력하기

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j:4}', end = '')
    print()
