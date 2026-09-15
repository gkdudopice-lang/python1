# 딕셔너리 : 별도의 키를 통해 각 요소를 접근할 수 있도록 만들어진 데이터타입
# {}로 선언, 각 요소는 쉼표(,)를 사용해 구분
# 키와 값의 한쌍으로 구성되고, 이 둘은 콜론(:)으로 구분
# [] 대괄호, {} 중괄호, () 소괄호

coffee_menu = {'Americano': 2500, 'Esspresso': 2500, 'Latte': 4000, 'Moca': 4500}
print(coffee_menu)
print(coffee_menu['Americano']) # 키로 값 확인
print(coffee_menu.get('Esspresso')) # 키로 값 확인

# 추가, 삭제, 키 존재 여부 확인
coffee_menu['ColdBrew'] = 5500 # 새로운 키와 값 추가
del coffee_menu['Americano'] # 키와 값 제거

for e in coffee_menu:
    print(f'키: {e}, 값: {coffee_menu[e]}')

# update 함수 사용하기: 딕셔너리 데이터를 한꺼번에 변경 가능
coffee_menu.update({'Americano': 3500, 'Esspresso': 3500, 'Latte': 4500, 'Moca': 5000, '스무디': 6000})
print(coffee_menu)

# 문제 1. 딕셔너리 생성 및 출력
# 학생 3명의 이름을 키로, 점수를 값으로 하는 딕셔너리 student_score를 만들고
# 전체를 출력하세요. (예: 철수 90, 영희 85, 민수 78)
student_score = {'철수': 90, '영희': 85, '민수': 78 }
print(student_score)

# 문제 2. 값 조회
# coffee_menu에서 "Moca"의 가격을 get()함수를 이용해 출력하세요.
# 만약 존재하지 않는 메뉴("Cappuccino")를 get()으로 조회하면 어떻게 되는지도 확인해보세요
print(coffee_menu.get('Moca'))
print(coffee_menu.get('Cappuccino')) # none이 나옴

# 문제 3. 추가와 삭제
# coffee_menu에 "Cappuccino": 4800을 새로 추가하고, "Moca"를 삭제한 뒤 결과를 출력하세요.
coffee_menu['Cappuccino'] = 4800
del coffee_menu['Moca']
print(coffee_menu)

# 문제 4. 반복문과 조건문 활용
# coffee_menu를 반복문으로 순회하면서, 가격이 4000원 이상인 메유만 '메뉴명 - 가격' 형태로 출력하세요.
for e in coffee_menu:
    if coffee_menu[e] >= 4000:
        print(f'{e} - {coffee_menu[e]}')

# 문제 5. update() 활용 및 키 존재 확인
# update() 함수를 사용해 coffee_menu의 모든 가격을 10% 인상하세요.
# (힌트: 반복문으로 새 딕셔너리를 만든 뒤 update()로 반영) 그리고
# 'in'연산자를 사용해 '라떼'라는 키가 존재하는지 확인하는 코드도 작성하세요
new_menu = {}
for e in coffee_menu:
    new_menu[e] = int(coffee_menu[e]*1.1)

coffee_menu.update(new_menu)
print(coffee_menu)

if 'Latte' in coffee_menu:
    print('키가 존재합니다.')
else:
    print('키가 없습니다.')

# 다른 방법
for key, value in coffee_menu.items():
    coffee_menu[key] = int(value * 1.1)
print(coffee_menu)




