from unicodedata import category

# 기본 메뉴 추가
# {} 중괄호를 사용해 선언, 가가 요소는 ,(쉽표)로 구분
# 키와 값음 :(콜론)으로 구분
# 딕셔너리 내부에 리스트를 가짐
import json
menu = {

'americano': ['coffee', 2000, '기본 커피 입니다.'],
    'espresso': ['coffee', 2500, '진한 커피 입니다.'],
    'latte': ['coffee', 4000, '우유가 들어있는 커피'],
    'green tea': ['tea', 4500, '녹차 입니다.'],
    'black tea': ['tea', 4500, '홍차 입니다']
}

# 전체 메뉴 조회
# def는 함수를 만드는 키워드
def print_menu():
    for e in menu:
        print(f'{e} - {menu[e]}')

# 개별 메뉴 조회
def get_menu(name):
    if name in menu:
        print(menu[name]) # 메뉴 딕셔너리에 전달 받은 이름이 있는지 확인
    else:
        print('찾는 메뉴가 없습니다.')

# 메뉴 추가
def pluse_menu(name, category, price, desc):
    if name not in menu:
        menu[name] = [category, int(price), desc]
        print(f'{name}메뉴가 추가 되었습니다.')
    else:
        print('메뉴가 이미 존재합니다.')

# 메뉴 삭제
def delete_menu(name): #조회했을 때 메뉴가 있다면
    if name in menu: #그 메뉴 삭제
        del menu[name]
        print(f'{name}메뉴가 삭제 되었습니다.')
    else:
        print('메뉴가 존재하지 않습니다.')

# 메뉴 수정
def alter_menu(name, category, price, desc):
    if name in menu: #조회했을 때 메뉴가 있다면
        menu[name] = [category, int(price), desc] #그 메뉴 수정
        print(f'{name}메뉴가 수정되었습니다.')
    else:
        print('메뉴가 존재하지 않습니다.')

# 파일에서 불러 오기
def load_menu():
    try: # 예외가 발생하기 쉬운 구간에 사용
        with open('menu.json', 'r', encoding='utf-8') as file:
            return json.load(file) #중요
    except FileNotFoundError:
        print('해당 파일이 존재하지 않습니다.')
    except json.JSONDecodeError:
        print('JSON 디코딩 실패')

#파일에 저장 하기
def save_menu():
    with open('menu.json', 'w', encoding='utf-8') as file:
        json.dump(menu, file, ensure_ascii=False, indent=4) # 아스키 코드 아니다, 들여쓰기 4칸
        print('menu.json 파일에 저장되었습니다.')

# 전체메뉴 만들기
# [1]전체 메뉴 보기 [2]개별 메뉴 조회 [3]메뉴 추가 [4]메뉴 삭제 [5]메뉴 수정 [6]로딩 [7]저장 [0]종료하기
while True:
    print('메뉴를 선택 하세요: ')
    choice = int(input('[1]전체 메뉴 [2]조회 [3]추가 [4]삭제 [5]수정 [6]로딩 [7]저장 [0]종료: '))

    if choice == 1:
        print_menu()
    elif choice == 2:
        name = input('메뉴 이름: ') # 이름 입력받고
        get_menu(name)  # 겟 메뉴 실행해주기, 메걔변수로 값을 전달
    elif choice == 3:
        name= input('이름: ')
        category = input('종류: ')
        price = input('가격: ')
        desc = input('설명입력: ') # 이름 카테고리 가격 디이에스씨 입력받고
        pluse_menu(name, category, price, desc) # 플러스 메뉴 실행해주기
    elif choice == 4:
        name = input('메뉴 이름: ') # 이름 받고
        delete_menu(name) # 딜리트 메뉴 실행
    elif choice == 5:
        name, category, price, desc = input('이름, 종류, 가격, 설명입력: ').split()
        alter_menu(name, category, price, desc)
    elif choice == 6:
        menu = load_menu()
    elif choice == 7:
        save_menu()
    elif choice == 0:
        print('프로그램을 종료합니다.')
        break
        # 묶어서 이름, 종류, 가격, 설명 만들면 띄어쓰기 안됨 따로따로 만드는게 좋을듯!


