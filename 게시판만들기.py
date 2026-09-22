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
            id VARCHAR(10) PRIMARY KEY,
            pwd VARCHAR(15),
            name VARCHAR(20),
            email VARCHAR(20),
            addr VARCHAR(50)
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
            id VARCHAR(10),
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
    email = input("이메일 : ")
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
            return id
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
def write_post(conn,current_user ):
    print("\n[게시글 작성]")
    title = input('제목을 입력하세요: ')
    content = input('내용을 입력하세요: ')
    writer = current_user  # 로그인한 사용자의 아이디를 작성자로 자동 지정
    reg_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cur = conn.cursor()
    try:
        sql = "INSERT INTO boardTable (title, content, writer, reg_date) VALUES (%s, %s, %s, %s)"
        cur.execute(sql, (title, content, writer, reg_date))
        conn.commit()
        print("게시글이 성공적으로 등록되었습니다!")
    except Exception as e:
        print(f"오류 발생 : {e}")
    finally:
        cur.close()
def view_posts(conn):
    print("[게시글 목록/조회 기능]")
    cur = conn.cursor()
    try:
        # userTable과 JOIN하여 작성자 아이디 대신 '이름(name)'을 가져옴 (최신순 정렬)
        sql = """
              SELECT b.board_id, b.title, u.name, b.reg_date
              FROM boardTable b
                       JOIN userTable u ON b.writer = u.id
              ORDER BY b.reg_date DESC \
              """
        cur.execute(sql)
        posts = cur.fetchall()

        if not posts:
            print("\n등록된 게시글이 없습니다.")
            return

        print("\n===== 게시글 목록 =====")
        print("번호 | 제목 \t\t| 작성자 | 작성일")
        print("-" * 45)
        for post in posts:
            print(f"{post[0]}    | {post[1]} \t| {post[2]}    | {post[3]}")
        print("=======================")

        # 상세 조회 여부 선택
        choice = input("\n상세 조회를 할 게시글 번호를 입력하세요 (메뉴로 돌아가려면 엔터): ")
        if choice.isdigit():
            view_post_detail(conn, int(choice))

    except Exception as e:
        print(f"오류 발생 : {e}")
    finally:
        cur.close()


# [기능 4-2] 게시글 상세 조회 및 댓글 출력 (STEP 4)
def view_post_detail(conn, board_id):
    cur = conn.cursor()
    try:
        # 1. 선택한 게시글 본문 조회
        sql = """
              SELECT b.title, b.content, u.name, b.reg_date, b.writer
              FROM boardTable b
                       JOIN userTable u ON b.writer = u.id
              WHERE b.board_id = %s \
              """
        cur.execute(sql, (board_id,))
        post = cur.fetchone()

        if not post:
            print("\n존재하지 않는 게시글 번호입니다.")
            return

        print(f"\n[게시글 상세 정보 (글번호: {board_id})]")
        print(f"제목 : {post[0]}")
        print(f"작성자 : {post[2]} ({post[4]})")
        print(f"작성일 : {post[3]}")
        print("-" * 40)
        print(f"내용:\n{post[1]}")
        print("-" * 40)

        # 2. 해당 글에 달린 댓글 목록 조회
        comment_sql = """
                      SELECT c.writer, c.content, c.reg_date
                      FROM commentTable c
                      WHERE c.board_id = %s
                      ORDER BY c.reg_date ASC \
                      """
        cur.execute(comment_sql, (board_id,))
        comments = cur.fetchall()

        print("[댓글 목록]")
        if not comments:
            print("작성된 댓글이 없습니다.")
        else:
            for com in comments:
                print(f"👉 {com[0]} : {com[1]}  ({com[2]})")
        print("==================================")

    except Exception as e:
        print(f"오류 발생 : {e}")
    finally:
        cur.close()

def write_comment(conn, current_user ):
    print("[댓글 작성 기능]")
    board_id = input("댓글을 달 게시글 번호를 입력하세요: ")
    if not board_id.isdigit():
        print("올바른 게시글 번호를 입력해주세요.")
        return

    cur = conn.cursor()
    try:
        # 1. 존재하는 게시글 번호인지 확인
        cur.execute("SELECT * FROM boardTable WHERE board_id = %s", (board_id,))
        if not cur.fetchone():
            print("오류 발생 : 존재하지 않는 게시글 번호입니다.")
            return

        # 2. 댓글 내용 입력받아 저장
        content = input("댓글 내용을 입력하세요: ")
        reg_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        sql = "INSERT INTO commentTable (board_id, writer, content, reg_date) VALUES (%s, %s, %s, %s)"
        cur.execute(sql, (board_id, current_user, content, reg_date))
        conn.commit()
        print("댓글이 성공적으로 등록되었습니다!")

    except Exception as e:
        print(f"오류 발생 : {e}")
    finally:
        cur.close()

def delete_post(conn, current_user ):
    print("[게시글 삭제 기능]")
    board_id = input("삭제할 게시글 번호를 입력하세요: ")
    if not board_id.isdigit():
        print("올바른 게시글 번호를 입력해주세요.")
        return

    cur = conn.cursor()
    try:
        # 1. 글의 작성자 확인
        cur.execute("SELECT writer FROM boardTable WHERE board_id = %s", (board_id,))
        post = cur.fetchone()

        if not post:
            print("오류 발생 : 존재하지 않는 게시글 번호입니다.")
            return

        writer_id = post[0].strip()  # 공백 제거 안전장치

        # 2. 로그인한 사람과 글쓴이가 같은지 비교
        if writer_id != current_user:
            print("권한 없음 : 자신이 작성한 글만 삭제할 수 있습니다.")
            return

        # 3. 외래키 제약조건 때문에 달린 댓글들을 먼저 삭제한 뒤 게시글 삭제
        cur.execute("DELETE FROM commentTable WHERE board_id = %s", (board_id,))
        cur.execute("DELETE FROM boardTable WHERE board_id = %s", (board_id,))
        conn.commit()
        print("게시글이 성공적으로 삭제되었습니다.")

    except Exception as e:
        print(f"오류 발생 : {e}")
    finally:
        cur.close()

def main():
    conn = get_connection()
    # create_user_table(conn)
    # create_board_table(conn)
    # create_comment_table(conn)
    conn.close()

    is_logged_in = False  # 최초 로그인 상태: 아니오 (False)
    logged_in_user = None

    while True:
        conn = get_connection()

        # [1] 로그인 상태가 아닐 때 (시작 메뉴)
        if not is_logged_in:
            print_auth_menu()
            choice = input("선택: ")

            if choice == "1":
                # 로그인 함수 실행 후, 성공하면 아이디를 리턴받음
                user_id = login_user(conn)
                if user_id:
                    is_logged_in = True
                    logged_in_user = user_id  # 로그인한 아이디 기억!
            elif choice == "2":
                signup_user(conn)  # 회원가입
            elif choice == "0":
                print("프로그램을 종료합니다.")
                conn.close()
                break
            else:
                print("잘못된 선택입니다. 다시 입력하세요.")

        # [2] 로그인 상태일 때 (게시판 메뉴)
        else:
            print_board_menu()
            choice = input("선택: ")

            if choice == "1":
                write_post(conn, logged_in_user)  # 게시글 작성 (기억한 아이디 전달)
            elif choice == "2":
                view_posts(conn)
            elif choice == "3":
                write_comment(conn, logged_in_user)
            elif choice == "4":
                delete_post(conn, logged_in_user)
            elif choice == "5":
                print("로그아웃 되었습니다.")
                is_logged_in = False
                logged_in_user = None  # 로그아웃 시 아이디 초기화
            else:
                print("잘못된 선택입니다. 다시 입력하세요.")

        conn.close()
if __name__ == "__main__":
    main()