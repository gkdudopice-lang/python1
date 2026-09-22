# 아래 조건에 맞는 도서 관리 프로그램을 작성하세요.
# **1단계. 데이터 구성**
#
# - 도서 정보를 담는 딕셔너리를 최소 5개 만들어 리스트로 구성하세요.
# - 각 도서는 다음 필드를 포함해야 합니다.
#     - `title` (문자열)
#     - `author` (문자열)
#     - `publisher` (문자열)
#     - `year` (정수)
#     - `price` (정수)
#     - `genre` (문자열 2개로 구성된 리스트)
import json
books = [
    {
        "title": "클린 코드",
        "author": "로버트 C. 마틴",
        "publisher": "인사이트",
        "year": 2013,
        "price": 33000,
        "genre": ["IT", "개발"]
    },
    {
        "title": "혼자 공부하는 파이썬",
        "author": "윤인성",
        "publisher": "한빛미디어",
        "year": 2022,
        "price": 22000,
        "genre": ["프로그래밍", "교육"]
    },
    {
        "title": "이것이 자바다",
        "author": "신용권",
        "publisher": "한빛미디어",
        "year": 2023,
        "price": 32000,
        "genre": ["IT", "프로그래밍"]
    },
    {
        "title": "어린왕자",
        "author": "생텍쥐페리",
        "publisher": "열린책들",
        "year": 2015,
        "price": 11500,
        "genre": ["소설", "문학"]
    },
    {
        "title": "코스모스",
        "author": "칼 세이건",
        "publisher": "사이언스북스",
        "year": 2006,
        "price": 45000,
        "genre": ["과학", "교양"]
    }
]
#
# **2단계. 직렬화**
#
# - 위 리스트를 `json.dumps()`를 사용해 JSON 문자열로 변환하고 출력하세요.
# - 한글이 깨지지 않도록 옵션을 설정하고, 보기 좋게 들여쓰기 하세요.
json.books = json.dumps(books, ensure_ascii=False, indent=4)
print(json.books)

# **3단계. 역직렬화**
#
# - 2단계에서 만든 JSON 문자열을 다시 Python 객체로 변환하세요.
# - `for`문을 사용해 각 도서 정보를 한 줄씩 출력하세요.
obj = json.loads(json.books)
print('--------------------')
for e in obj:
    print(e)
print('--------------------')

# **4단계. 데이터 가공 (응용)**
#
# - 역직렬화한 데이터에서 **가격이 30,000원 이상인 책만** 필터링하세요.
# - 필터링한 결과를 `"제목 - 가격원"` 형식으로 출력하세요. (예: `클린 코드 - 33,000원`)
for e in obj:
    if e['price'] >= 30000:
        print(f'{e['title']} - {e['price']:,}원')

# **5단계. 파일 저장 및 읽기**
#
# - 전체 도서 리스트를 `books.json` 파일로 저장하세요.
# - 저장한 파일을 다시 읽어서 출력하세요.
with open('books.json', 'w', encoding='utf-8') as f:
    json.dump(books, f, ensure_ascii=False, indent=4)

with open('books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)

# **6단계. 심화 (선택)**
#
# - `books.json`을 읽은 후, 사용자로부터 저자 이름을 입력받아 해당 저자의 책만 출력하는 기능을 추가하세요.
search_author = input('저자의 이름을 입력하세요: ')
with open('books.json', 'r', encoding='utf-8') as f:
    books_f_file = json.load(f)

found = False

for books in books_f_file:
    if books['author'] == search_author:
        print(f'검색결과: {books["title"]} - {books["author"]}')
        found = True

if not found:
    print('저자의 이름을 다시 확인해주세요.')


