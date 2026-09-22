import pymysql
from datetime import datetime

# 1. DB 연결
def get_connection():
    conn = pymysql.connect(host="127.0.0.1", user="root", port=3306,
                           password="1234", database="mysqlDB", charset="utf8")
    return conn

# 2. 테이블 생성 함수들
def create_user_table(conn):
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS commentTable")
    cur.execute("DROP TABLE IF EXISTS boardTable")
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
    cur.close()

def create_board_table(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE boardTable (
            board_id BIGINT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(50) NOT NULL,
            content TEXT,
            id CHAR(10),
            writer CHAR(10),
            reg_date datetime,
            FOREIGN KEY (writer) REFERENCES userTable(id)
        )
    """)
    conn.commit()
    cur.close()

def create_comment_table(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE commentTable (
            comment_id BIGINT AUTO_INCREMENT PRIMARY KEY,
            board_id BIGINT,
            id CHAR(10),
            writer CHAR(10),
            content VARCHAR(1000),
            reg_date datetime,
            FOREIGN KEY (board_id) REFERENCES boardTable(board_id),
            FOREIGN KEY (writer) REFERENCES userTable(id)
        )
    """)
    conn.commit()
    cur.close()


#회원가입
def signup_user(conn):
    cur = conn.cursor()
    id = input("아이디 : ")
    if id == 'exit': return "exit"
    pwd = input("패스워드 : ")
    name = input("이름 : ")
    mail = input("이메일 : ")
    addr = input("주소 : ")

    register_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        sql = "INSERT INTO userTable (id, pwd, name, email, addr) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql, (id, pwd, name, email, addr))
        conn.commit()
        print("성공적으로 회원가입이 되었습니다.")

    except pymysql.err.IntegrityError as e:
        # MySQL 중복 키 에러 번호인 1062번 확인
        if e.args[0] == 1062:
            print("오류 발생 : 이미 존재하는 아이디입니다.")
        else:
            print(f"오류 발생 : {e}")

    except Exception as e:
        print(f"오류 발생 : {e}")

    finally:
        cur.close()

# 1. 로그인 함수
def login_user(conn):
    cur = conn.cursor()
    print("\n--- 로그인 ---")
    id = input("아이디 : ")
    pwd = input("패스워드 : ")

    try:
        sql = "SELECT * FROM userTable WHERE id = %s AND pwd = %s"
        cur.execute(sql, (id, pwd))
        user = cur.fetchone()

        if user:
            print(f"로그인 성공! 환영합니다, {user[0]}님.") # name 컬럼 위치에 따라 인덱스 조정 가능
            return True
        else:
            print("로그인 실패 : 이메일 또는 비밀번호가 잘못되었습니다.")
            return False
    finally:
        cur.close()

# 2. 비로그인 상태 메뉴 (회원가입 / 로그인)
def print_auth_menu():
    print("\n===== 시작 메뉴 =====")
    print("1. 로그인")
    print("2. 회원가입")
    print("0. 프로그램 종료")
    print("====================")

# 3. 로그인 상태 게시판 메뉴
def print_board_menu():
    print("\n===== 게시판 메뉴 =====")
    print("1. 게시글 작성")
    print("2. 게시글 목록/조회")
    print("3. 댓글 작성")
    print("4. 게시글 삭제")
    print("5. 로그아웃")
    print("=======================")

# 4. 게
def write_post(conn):
    print("[게시글 작성 기능]")
    pass
def view_posts(conn):
    print("[게시글 목록/조회 기능]")
    pass
def write_comment(conn):
    print("[댓글 작성 기능]")
    pass
def delete_post(conn):
    print("[게시글 삭제 기능]")
    pass

def main():
    conn = get_connection()
    create_user_table(conn)
    create_board_table(conn)
    create_comment_table(conn)
    conn.close()

    is_logged_in = False  # 최초 로그인 상태: 아니오 (False)

    while True:
        conn = get_connection()

        # 로그인 상태 확인
        if not is_logged_in:
            print_auth_menu()
            choice = input("선택: ")

            if choice == "1":
                # 로그인 시도
                if login_user(conn):
                    is_logged_in = True  # 로그인 성공 시 상태 변경
            elif choice == "2":
                # 회원가입
                signup_user(conn)
            elif choice == "0":
                print("프로그램을 종료합니다.")
                conn.close()
                break
            else:
                print("잘못된 선택입니다. 다시 입력하세요.")

        else:
            # 플로우차트 D: 로그인 상태가 '예'일 때 게시판 메뉴 노출
            print_board_menu()
            choice = input("선택: ")

            if choice == "1":
                write_post(conn)
            elif choice == "2":
                view_posts(conn)
            elif choice == "3":
                write_comment(conn)
            elif choice == "4":
                delete_post(conn)
            elif choice == "5":
                print("로그아웃 되었습니다.")
                is_logged_in = False  # 로그아웃 시 다시 비로그인 상태로 전환
            else:
                print("잘못된 선택입니다. 다시 입력하세요.")

        conn.close()

if __name__ == "__main__":
    main()