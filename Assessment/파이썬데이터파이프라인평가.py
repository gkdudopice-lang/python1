file_name = './order.txt'
total_sales = 0

try:
    with open(file_name, 'r', encoding='utf-8') as file:

        for e in file:
            data_list = e.strip().split(',')

            menu = data_list[0].strip()
            quantity = int(data_list[1].strip())
            price = int(data_list[2].strip().replace('원', ''))

            if price < 0:
                continue
            elif price > 10000:
                continue
            elif quantity < 0:
                continue
            total_sales += (quantity * price)

        print(f'총 매출액: {total_sales}원')

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")