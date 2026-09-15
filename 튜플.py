# 파이썬에서 튜플(tuple)은 변경할 수 없는(immutable) 시퀀스 자료형입니다.
# 튜플은 여러 개의 요소를 저장하고, 각 요소에는 인덱스를 통해 접근할 수 있습니다.
# 튜플은 괄호(())를 사용하여 정의하며, 각 요소는 쉼표(,)로 구분됩니다.

ls = [1, 2, 3]
tp1 = (1, 2, 3)
tp2 = 1, 2, 3
ts = 1
ts2 = '1'
ts3 = 1,
print(type(ls))
print(type(tp1))
print(type(tp2))
print(type(ts))
print(type(ts2))
print(type(ts3)) # 이건 튜플 (콤마 땜시)

member = '안유진', 23, '대전시', True # 패킹
name, age, addr, is_adult = member # 언패킹

# member.append('1004') # 이거 안됨 튜플에는 어팬드 못씀
# print(member)

def get_name_card(name, phone):
    position = f'{name} 수석연구원'
    addr = '서울시 강남구'
    phone = f'082+{phone}'
    return position, addr, phone

result = get_name_card('곰돌이', '1234-5678')
print(f'{result}')

s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])

# 중복 제거
s3 = set([1,2,3,4,5,6,2,3,4,5])
print(s3)

# 교집합
print(s1.intersection(s2))
(s1 & s2)

# 합집합
print(s1.union(s2))
print(s1 | s2)

# 차집합
print(s1.difference(s2))
print(s1 - s2)

