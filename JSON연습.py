# JSON(JacaScript Object Notation)은 데이터를 저장하고 교환하는데 널리 사용되는 경량 텍스트 형식이다
# - 파이썬에서는 json기본 라이브러리를 통해 사용 가능
# - 경량 텍스트 포맷
# - 키와 값으로 구성
# - 언어 독립적
# - 웹 API통신, 설정파일, 데이터 저장 및 교환 등 다양한 분야에서 활용
import json

# 파이썬 객체를 json으로 직렬화
# 회원 정보(이름, 주소, 나이, 성별, 포지션, 전화번호 2개) => 딕셔너리
# 회원 정보가 10개인 리스트 => 리스트

members = [
    {
        'name': '안유진',
        'addr': '대전시',
        'age': 23,
        'gender': '여성',
        'position': '리더',
        'phone': ['010-1234-5678', '041-123-4556']
    },
    {
        'name': '리즈',
        'addr': '천안시',
        'age': 24,
        'gender': '여성',
        'position': '멤버',
        'phone': ['010-1235-5678', '041-129-4556']

    },
    {
        'name': '장원영',
        'addr': '경기도',
        'age': 25,
        'gender': '여성',
        'position': '멤버',
        'phone': ['010-1035-5678', '041-159-4556']
    },
    {
        'name': '가을',
        'addr': '대전시',
        'age': 26,
        'gender': '여성',
        'position': '멤버',
        'phone': ['010-1235-5978', '041-119-4556']
    },
    {
        'name': '레이',
        'addr': '일본',
        'age': 27,
        'gender': '여성',
        'position': '멤버',
        'phone': ['010-1225-5678', '041-129-4506']
    }

]

# Python 객체를 JSON으로 직렬화
json_str = json.dumps(members, ensure_ascii=False, indent=4)
print(json_str)

# JSON을 -> Python으로 역직렬화
obj = json.loads(json_str)
print(obj)

print('--------------------------')
for e in obj:
    print(e)
print('--------------------------')

# 파일로 저장 하기
# with는 파일을 자동으로 닫아줌
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(members, json_file, ensure_ascii=False, indent=4)

# 파일에서 읽기
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

print(data)








