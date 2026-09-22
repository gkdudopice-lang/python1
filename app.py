import datetime
from flask import Flask, jsonify, Response, request, render_template
import json
import requests  # http 통신
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def get_index():
    return "<h1>파이썬 Flask에서 온신걸 환영 합니다.</h1>"

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/weather", methods=['GET'])
def get_weather():
    print("GET 요청을 받았습니다.")
    nx_val = request.args.get('x', default=None, type=None)
    ny_val = request.args.get('y', default=None, type=None)
    print("X : ", nx_val)
    print("Y : ", ny_val)
    API_KEY = 'LPh8U0fWWitEfCUYAQMCreTSbSbI4XqYB+spk2jhS90QAcvAT1FforFEAfawd9rL4yV8Ecqs+0pv6G9eMYM5yA=='

    # 요청 주소의 URL 지정
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'

    # 날짜 및 시간 설정
    now = datetime.datetime.now()  # 운영체제로 현재 시간과 날짜 정보를 가져 옴

    # 년월일 정보를 추출하기 위해서 포맷 형식을 지정, base_date : 20240121
    date = now.strftime('%Y%m%d')

    # 시간 정보를 추출하기 위해서 포맷 형식을 지정, base_time : 0622
    if now.minute < 30:  # 현재 분이 30분 이전이면 전 시간으로 설정
        now = now - datetime.timedelta(minutes=30)
        time = now.strftime('%H%M')
    else:
        time = now.strftime('%H%M')

    # 예보 지점 좌표 (서울시 강남구 역삼동)
    # nx_val = 62
    # ny_val = 126

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

    # 딕셔너리 데이터를 분석하여 원하는 데이터를 추출
    weather_items = dict_data['response']['body']['items']['item']

    weather_data = {}

    for k in range(len(weather_items)):
        weather_item = weather_items[k]
        obsrValue = weather_item['obsrValue']
        if weather_item['category'] == 'T1H':
            weather_data['tmp'] = f"{obsrValue}℃"
        elif weather_item['category'] == 'REH':
            weather_data['hum'] = f"{obsrValue}%"
        elif weather_item['category'] == 'RN1':
            weather_data['pre'] = f"{obsrValue}mm"
        # 딕셔너리를 JSON 형태로 변환
    json_weather = json.dumps(weather_data, ensure_ascii=False, indent=4)
    return json_weather

# 서버 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
