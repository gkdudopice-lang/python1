import pymysql

# 1. DB 연결
def get_connection():
    conn = pymysql.connect(host="127.0.0.1", user="root", port=3306,
                           password="1234", database="mysqlDB", charset="utf8")
    return conn

def create_user_table(conn):
    cur = conn.cursor()

    # 2. 기존 테이블 삭제 및 생성
    cur.execute("DROP TABLE IF EXISTS userTable")
    cur.execute("""
        CREATE TABLE userTable (
            id CHAR(10) PRIMARY KEY,
            pwd CHAR(15),
            name CHAR(20),
            email CHAR(20),
            addr CHAR(50)
        )
    """)
    conn.commit()
    conn.close()

# 3. 초기 데이터 삽입
def insert_user(conn):
    cur = conn.cursor()
    users = [
        ('ayj1234', '12345678', '안유진', 'ayj@gmail.com', '서울시 강남구'),
        ('jwy1234', '12345678', '장원영', 'jwy@gmail.com', '서울시 강남구'),
        ('fall1234', '12345678', '가을', 'fall@gmail.com', '서울시 강남구'),
        ('ys1234', '12345678', '이서', 'ws@gmail.com', '서울시 강남구'),
        ('lay1234', '12345678', '레이', 'lay@gmail.com', '서울시 강남구'),
        ('liz1234', '12345678', '리즈', 'liz@gmail.com', '서울시 강남구')
    ]

    for user in users:
        cur.execute("INSERT INTO userTable VALUES(%s, %s, %s, %s, %s)", user)

    # 4. 커밋 및 연결 종료
    conn.commit()
    conn.close()
# 신규 회원 추가
def new_user_insert(conn):
    cur = conn.cursor()
    id = input("아이디 : ")
    if id == 'exit': return "exit"
    pwd = input("패스워드 : ")
    name = input("이름 : ")
    mail = input("이메일 : ")
    addr = input("주소 : ")
    try:
        cur.execute("INSERT INTO userTable VALUES(%s, %s, %s, %s, %s)", (id, pwd, name, mail, addr))
    except Exception as e:
        print(f"오류 발생 : {e}")

    conn.commit()
    conn.close()

# 회원 수정
def update_user(conn):
    cur = conn.cursor()
    id = input('수정할 ID: ')
    name = input('새로운 이름: ')
    email = input('새로운 이메일: ')
    addr = input('새로운 주소: ')

    try:
        cur.execute('UPDATE userTable SET name=%s, email=%s, addr=%s WHERE id=%s', (name, email, addr, id))
        if cur.rowcount > 0:
            print('수정 완료!')
        else:
            print('해당 ID가 존재하지 않습니다.')
        conn.commit()
    except Exception as e:
        print(f'오류 발생: {e}')
    finally:
        cur.close()
# 회원 삭제
def delete_user(conn):
    cur = conn.cursor()
    id = input('삭제할 ID')

    try:
        cur.execute('DELETE FROM userTable WHERE id=%s', (id,))
        # [설명] userTable에서 입력받은 id와 일치하는 데이터를 삭제(`DELETE`)하라는 SQL 실행
        # (주의: 매개변수가 1개여도 괄호 안에서 콤마를 찍어 튜플 형태로 전달하는 것이 안전합니다: (id,))

        if cur.rowcount > 0:
            print('삭제 성공!')
        else:
            print('해당 ID가 존재하지 않습니다.')

        conn.commit()
    except Exception as e:
        print(f'오류 발생 : {e}')
    finally:
        cur.close()

# 회원 조회
def search_user(conn):
    cur = conn.cursor()
    id = input('조회할 회원의 ID: ')

    try:
        cur.execute('SELECT * FROM userTable WHERE id=%s', (id,))
        row = cur.fetchone()
        # [설명] 조건에 맞는 데이터 '딱 한 줄'을 가져와서 row 변수에 담습니다.
        # (ID는 PRIMARY KEY라 중복이 없으므로 fetchone()을 씁니다.)

        if row:
            print("\n[조회 결과]")
            print(f"아이디 : {row[0]}")
            print(f"비밀번호 : {row[1]}")
            print(f"이름 : {row[2]}")
            print(f"이메일 : {row[3]}")
            print(f"주소 : {row[4]}")
        else:
            print('해당 ID가 존재하지 않습니다.')

    except Exception as e:
        print(f"오류 발생 : {e}")
    finally:
        cur.close()

# 사용자 전체 조회
def search_all_user():
    cur = conn.cursor()

    try:
        cur.execute('SELECT * FROM userTable')  # userTable의 모든 데이터를 선택
        rows = cur.fetchall()  # 조건에 맞는 '모든 행'을 리스트 형태로 가져옴

        if rows:  # 데이터가 존재한다면
            print("\n===== 전체 회원 목록 =====")
            print("아이디\t\t비밀번호\t이름\t이메일\t\t\t주소")
            print("-" * 50)
            for row in rows:  # [질문하신 부분!] 여러 행을 반복문으로 하나씩 꺼냄
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")
            print("============================")
        else:
            print('등록된 회원이 없습니다.')

    except Exception as e:
        print(f"오류 발생 : {e}")
    finally:
        cur.close()

# 메뉴 출력
def print_menu():
    print("\n===== 사용자 관리 메뉴 =====")
    print("1. 사용자 추가")
    print("2. 사용자 수정")
    print("3. 사용자 삭제")
    print("4. 사용자 조회")
    print("5. 사용자 전체 조회")
    print("0. 종료")
    print("============================")

def main():
    conn = get_connection() # DB 연결
    create_user_table(conn) # 테이블 생성
    conn = get_connection() # DB 연결
    insert_user(conn)       # 초기 회원 정보 삽입

    while True:
        conn = get_connection()
        print_menu()
        choice = input('선택: ')

        if choice == '1':
            insert_user(conn)
        elif choice == '2':
            update_user(conn)
        elif choice == '3':
            delete_user(conn)
        elif choice == '4':
            search_user(conn)
        elif choice == '5':
            pass
        elif choice == '0':
            print('프로그램을 종료합니다.')
            conn.close()
            break
        else:
            print('잘못된 선택입니다. 다시 입력 해 주세요')

if __name__ == "__main__":
    main()