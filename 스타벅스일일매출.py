# 상대경로가 유리함 절대경로는 다른곳에서 하면 작동 안함
# r = read, w = write, a = append / t = text, b = binary
# with open('./스타벅스일일매출.txt', 'r', encoding='utf-8') as file:
#     for e in file:
#         print(e, end='') # 한줄한줄 엔터키 기준으로 줄 바꿔줌
#     print()

# 스타벅스 판매량 구하기
file_name = '스타벅스일일매출.txt'
espresso = [] # 빈 리스트 생성
americano = []
cafelatte = []
cappuccino = []
dates = []

with open(file_name, 'r', encoding='utf-8') as file:
    header = file.readline().split() # 줄 바꿈 기준으로 한 줄을 읽어 들임
                                     # 공백 기준으로 잘라 문자열 리스트 생성

    for e in file:
        data_list = e.split() # 데이터 첫 줄 부터 마지막 줄 까지 불러들임
        dates.append(data_list[0])
        espresso.append(int(data_list[1])) # 10
        americano.append(int(data_list[2])) # 50
        cafelatte.append(int(data_list[3]))  # 45
        cappuccino.append(int(data_list[4]))  # 20

# 제목 / 전체 판매량 / 일 평균 판매량
print('제목\t\t\t   전체 판매량\t\t 일 평균 판매량')
print('-----------------------------------------------')
print(f'{header[1]:8} {sum(espresso):11} {sum(espresso) / len(espresso):19}')
print(f'{header[2]:8} {sum(americano):11} {sum(americano) / len(americano):19.2f}')
print(f'{header[3]:8} {sum(cafelatte):11} {sum(cafelatte) / len(cafelatte):19}')
print(f'{header[4]:8} {sum(cappuccino):11} {sum(cappuccino) / len(cappuccino):19.2f}')

# 1. 각 메뉴별 전체 판매량
def total_sales_func():
    print(f'{header[1]} = {sum(espresso)}')
    print(f'{header[2]} = {sum(americano)}')
    print(f'{header[3]} = {sum(cafelatte)}')
    print(f'{header[4]} = {sum(cappuccino)}')
    print("----------------------------------------")

# 2. 각 메뉴별 일 평균 판매량
def avg_sales_func():
    print(f'{header[1]} = {sum(espresso) / len(espresso)}')
    print(f'{header[2]} = {sum(americano) / len(americano):.2f}')
    print(f'{header[3]} = {sum(cafelatte) / len(cafelatte)}')
    print(f'{header[4]} = {sum(cappuccino) / len(cappuccino):.2f}')
    print("----------------------------------------")

# 3. 판매량이 가장 높은 메뉴 구하기
def most_sold_func():
    total = [sum(espresso), sum(americano), sum(cafelatte), sum(cappuccino)]
    max_value = max(total)
    max_index = total.index(max_value)
    print(f'가장 많이 팔린 메뉴는 "{header[max_index + 1]}" {max_value}개')
    print("----------------------------------------")

# 4. 판매량이 가장 적은 메뉴 구하기
def least_sold_func():
    total = [sum(espresso), sum(americano), sum(cafelatte), sum(cappuccino)]
    min_value = min(total)
    min_index = total.index(min_value)
    print(f'가장 적게 팔린 메뉴는 "{header[min_index + 1]}" {min_value}개')
    print("----------------------------------------")

# 5. 판매량이 가장 많은 날짜 구하기
def best_sales_day_func():
    total = [sum(espresso) / len(espresso), sum(americano) / len(americano), sum(cafelatte) / len(cafelatte), sum(cappuccino) / len(cappuccino)]
    best_sales_value = max(total)
    best_sales_index = total.index(best_sales_value)
    print(f'판매량이 가장 많은 날은 "{dates[best_sales_index]}" {best_sales_value}이다.')
    print("----------------------------------------")
    # 위에꺼 다른 방법
# def best_sales_day_func():
#     total_per_day = []
#     for i in range(len(dates)):
#         total = espresso[i] + americano[i] + cafelatte[i] + cappuccino[i]
#         total_per_day.append(total)
#     max_sales = max(total_per_day)
#     max_idex = total_per_day.index(max_sales)

# 6. 반복문으로 구성된 메뉴 만들기
while True:
    print('[1] 각 메뉴별 전체 판매량')
    print('[2] 각 메뉴별 일 평균 판매량')
    print('[3] 판매량이 가장 높은 메뉴 보기')
    print('[4] 판매량이 가장 적은 메뉴 보기')
    print('[5] 판매량이 가장 많은 날짜')
    print('[0] 종료')
    choice = int(input('원하는 메뉴를 선택하세요: '))

    if choice == 1:
        total_sales_func()
    elif choice == 2:
        avg_sales_func()
    elif choice == 3:
        most_sold_func()
    elif choice == 4:
        least_sold_func()
    elif choice == 5:
        best_sales_day_func()
    elif choice == 0:
        print('프로그램을 종료합니다.')
        break
    else:
        print('유효한 번호를 입력하세요')
        print("----------------------------------------")
