
import requests # HTTP로 서버의 데이터를 수신하기 위해서 사용
import json # 정부기관 공공데이터를 JSON형태로 수신 받기 위함
import datetime # 시간 정보를 구하기 위해서

API_KEY = '0833cc3dbb564e6d136da268c44280a90d9cf83ad024ad4cc1e51cd6b66356be'

# 요청 주소의 URL 지정
url = 'https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'

# 날짜 및 시간 설정
now = datetime.datetime.now() # 운영체제로 현재 시간과 날짜 정보를 가져옴

# 년월일 정보를 추출하기 위해서 포맷 형식을 지정, base_date : 20260921
date = now.strftime('%Y%m%d')

# 시간 정보를 추출하기 위해서 포맷 형식을 지정, base_time : 0622
if now.minute < 30: # 현재 분이 30분 이전이면 전 시간으로 설정
    now = now - datetime.timedelta(minutes=30)
    time = now.strftime('%H%M')
else:
    time = now.strftime('%H%M')

# 예보 지점 좌표 ( 천안시 동남구 신안동)
nx_val = 63
ny_val = 110

# 한 페이지에 포함된 결과 수
num_of_rows = 6
# 페이지 번호
page_no = 1
# 응답 데이터 형식 지정
data_type = 'JSON'

req_parameter = {'serviceKey': API_KEY,
                 'pageNo': page_no,
                 'numOfRows': num_of_rows,
                 'dataType': data_type,
                 'base_date': date,
                 'base_time': time,
                 'nx': nx_val, 'ny': ny_val
                 }
# 요청 및 응답 : 서버로 부터 데이터를 수신 받기 때문에 예외 처리가 필요
response = ""
try:
    response = requests.get(url, params=req_parameter)
except requests.exceptions.RequestException as e:
    print(f"날씨 정보 가져 오기 오류 : {e}")

# JSON 형태로 응답받은 데어터를 딕셔너리로 변환 (역직렬화)
dict_data = response.json()
print(json.dumps(dict_data, indent=2))

# 딕셔너리 데이터를 분석하여 원하는 데이터를 추출
weather_items = dict_data['response']['body']['items']['item']

for weather_item in weather_items:
    obsrValue = weather_item['obsrValue']
    category = weather_item['category']
    if category == 'T1H':
        print(f"[현재 기온 : {obsrValue}℃]")
    elif category == 'REH':
        print(f"[현재 습도 : {obsrValue}%]")
    elif category == 'RN1':
        print(f"[1시간 강수량 : {obsrValue}mm]")







