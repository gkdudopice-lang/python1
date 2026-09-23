import pymysql
from datetime import datetime

# 1. DB 연결
def get_connection():
    conn = pymysql.connect(host="127.0.0.1", user="root", port=3306,
                           password="1234", database="mysqlDB", charset="utf8")
    return conn


def create_tables(conn):
    cur = conn.cursor()

    try:
        # 1. userTable 생성
        cur.execute(
            "CREATE TABLE IF NOT EXISTS userTable (id CHAR(10) PRIMARY KEY, pwd CHAR(15), name CHAR(20), email CHAR(20), addr CHAR(50))")

        # 2. boardTable 생성
        cur.execute(
            "CREATE TABLE IF NOT EXISTS boardTable (board_id BIGINT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(50) NOT NULL, content TEXT, writer CHAR(10), reg_date DATETIME, FOREIGN KEY (writer) REFERENCES userTable(id))")

        # 3. commentTable 생성
        cur.execute(
            "CREATE TABLE IF NOT EXISTS commentTable (comment_id BIGINT AUTO_INCREMENT PRIMARY KEY, board_id BIGINT, writer CHAR(10), content VARCHAR(1000), reg_date DATETIME, FOREIGN KEY (board_id) REFERENCES boardTable(board_id), FOREIGN KEY (writer) REFERENCES userTable(id))")

        conn.commit()
    finally:
        cur.close()

# 회원가입
def signup_user(conn):
    cur = conn.cursor()
    id = input("아이디 : ")
    if id == 'exit': return "exit"
    pwd = input("패스워드 : ")
    name = input("이름 : ")
    email = input("이메일 : ")
    addr = input("주소 : ")

    try:
        sql = "INSERT INTO userTable (id, pwd, name, email, addr) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql, (id, pwd, name, email, addr))
        conn.commit()
        print("성공적으로 회원가입이 되었습니다.")

    except pymysql.err.IntegrityError as e:
        if e.args[0] == 1062:
            print("오류 발생 : 이미 존재하는 아이디입니다.")
        else:
            print(f"오류 발생 : {e}")

    except Exception as e:
        print(f"오류 발생 : {e}")

    finally:
        cur.close()

# 로그인 함수 (성공 시 해당 아이디를 반환)
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
            print(f"로그인 성공! 환영합니다, {user[2]}님.")
            return id  # 로그인된 아이디 반환
        else:
            print("로그인 실패 : 아이디 또는 비밀번호가 잘못되었습니다.")
            return None
    finally:
        cur.close()

def print_auth_menu():
    print("\n===== 시작 메뉴 =====")
    print("1. 로그인")
    print("2. 회원가입")
    print("0. 프로그램 종료")
    print("====================")

def print_board_menu():
    print("\n===== 게시판 메뉴 =====")
    print("1. 게시글 작성")
    print("2. 게시글 목록/조회")
    print("3. 댓글 작성")
    print("4. 게시글 삭제")
    print("5. 로그아웃")
    print("=======================")

# 게시글 작성 (로그인된 아이디를 받아 userTable 외래키 참조 조건 만족)
def write_post(conn, login_id):
    print("\n--- 게시글 작성 ---")
    title = input("제목 : ")
    content = input("내용 : ")
    reg_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cur = conn.cursor()
    try:
        sql = """
              INSERT INTO boardTable (title, content, writer, reg_date)
              SELECT %s, %s, id, %s
              FROM userTable
              WHERE id = %s
              """
        cur.execute(sql, (title, content, reg_date, login_id))

        if cur.rowcount > 0:
            conn.commit()
            print("게시글이 성공적으로 등록되었습니다.")
        else:
            conn.rollback()
            print("오류 발생 : 회원 정보를 참조할 수 없습니다.")

    except Exception as e:
        conn.rollback()
        print(f"오류 발생 : {e}")

    finally:
        cur.close()

def view_posts(conn):
    cur = conn.cursor()
    try:
        # 1. 전체 게시글 목록 출력
        print("\n================ [게시글 목록] ================")
        sql = "SELECT board_id, title, writer, reg_date FROM boardTable ORDER BY board_id DESC"
        cur.execute(sql)
        posts = cur.fetchall()

        if not posts:
            print("등록된 게시글이 없습니다.")
            return

        print(f"{'번호':<6} | {'제목':<20} | {'작성자':<10} | {'작성일'}")
        print("-" * 55)
        for post in posts:
            board_id, title, writer, reg_date = post
            print(f"{board_id:<6} | {title:<20} | {writer:<10} | {reg_date}")
        print("=" * 55)

        # 2. 상세 조회 여부 선택
        choice = input("\n상세 조회할 게시글 번호를 입력하세요 (목록으로 돌아가려면 엔터): ").strip()
        if not choice:
            return

        # 3. 선택한 게시글 상세 내용 출력
        detail_sql = "SELECT board_id, title, content, writer, reg_date FROM boardTable WHERE board_id = %s"
        cur.execute(detail_sql, (choice,))
        post_detail = cur.fetchone()

        if not post_detail:
            print("존재하지 않는 게시글 번호입니다.")
            return

        b_id, b_title, b_content, b_writer, b_date = post_detail
        print(f"\n================ [게시글 상세] ================")
        print(f"글번호 : {b_id}")
        print(f"제  목 : {b_title}")
        print(f"작성자 : {b_writer}")
        print(f"작성일 : {b_date}")
        print(f"내  용 :\n{b_content}")
        print("-" * 45)

        # 4. 해당 게시글에 달린 댓글 목록 출력
        comment_sql = "SELECT writer, content, reg_date FROM commentTable WHERE board_id = %s ORDER BY comment_id ASC"
        cur.execute(comment_sql, (b_id,))
        comments = cur.fetchall()

        print("[ 댓글 목록 ]")
        if not comments:
            print("작성된 댓글이 없습니다.")
        else:
            for c_writer, c_content, c_date in comments:
                print(f" - {c_writer} : {c_content} ({c_date})")
        print("=============================================")

    except Exception as e:
        print(f"조회 중 오류 발생 : {e}")

    finally:
        cur.close()
# 댓글 작성
def write_comment(conn, login_id):
    print("\n--- 댓글 작성 ---")
    board_id = input("댓글을 달 게시글 번호 : ")
    content = input("댓글 내용 : ")
    reg_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cur = conn.cursor()
    try:
        sql = """
              INSERT INTO commentTable (board_id, writer, content, reg_date)
              SELECT %s, id, %s, %s 
              FROM userTable 
              WHERE id = %s
              """
        cur.execute(sql, (board_id, content, reg_date, login_id))

        if cur.rowcount > 0:
            conn.commit()
            print("댓글이 성공적으로 등록되었습니다.")
        else:
            conn.rollback()
            print("오류 발생 : 회원 정보를 찾을 수 없습니다.")

    except Exception as e:
        conn.rollback()
        print(f"오류 발생 : {e}")

    finally:
        cur.close()

# 게시글 삭제 (로그인된 사용자가 자신이 쓴 글만 삭제 가능하도록 비교)
def delete_post(conn, login_id):
    print("\n--- 게시글 삭제 ---")
    cur = conn.cursor()
    board_id = input("삭제할 게시글 번호(ID): ")

    try:
        check_sql = "SELECT title, writer FROM boardTable WHERE board_id = %s"
        cur.execute(check_sql, (board_id,))
        post = cur.fetchone()

        if not post:
            print("삭제할 게시물이 존재하지 않습니다.")
            return False

        title, writer = post[0], post[1].strip()

        # 로그인한 사용자가 쓴 글인지 확인
        if writer != login_id:
            print("오류 발생 : 권한이 없습니다. (자신이 쓴 글만 삭제할 수 있습니다.)")
            return False

        print(f"조회된 게시글 -> 제목: '{title}' (작성자: {writer})")

        confirm = input("정말 이 게시글과 관련된 댓글들을 삭제하시겠습니까? (y/n): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("게시글 삭제가 취소되었습니다.")
            return False

        sql_comment = "DELETE FROM commentTable WHERE board_id = %s"
        cur.execute(sql_comment, (board_id,))

        sql_board = "DELETE FROM boardTable WHERE board_id = %s"
        cur.execute(sql_board, (board_id,))

        conn.commit()
        print("게시물과 관련된 댓글이 모두 삭제되었습니다.")
        return True

    except Exception as e:
        conn.rollback()
        print(f"오류 발생 : {e}")
        return False

    finally:
        cur.close()

def main():
    conn = get_connection()
    create_tables(conn)
    conn.close()

    is_logged_in = False
    current_user_id = None

    while True:
        conn = get_connection()

        if not is_logged_in:
            print_auth_menu()
            choice = input("선택: ")

            if choice == "1":
                user_id = login_user(conn)
                if user_id is not None:
                    is_logged_in = True
                    current_user_id = user_id  # 로그인 성공 시 아이디 보관
            elif choice == "2":
                signup_user(conn)
            elif choice == "0":
                print("프로그램을 종료합니다.")
                conn.close()
                break
            else:
                print("잘못된 선택입니다. 다시 입력하세요.")

        else:
            print_board_menu()
            choice = input("선택: ")

            if choice == "1":
                write_post(conn, current_user_id)  # 로그인 아이디 전달
            elif choice == "2":
                view_posts(conn)
            elif choice == "3":
                write_comment(conn, current_user_id)  # 로그인 아이디 전달
            elif choice == "4":
                delete_post(conn, current_user_id)  # 로그인 아이디 전달 (본인 글 검증)
            elif choice == "5":
                print("로그아웃 되었습니다.")
                is_logged_in = False
                current_user_id = None  # 로그아웃 시 초기화
            else:
                print("잘못된 선택입니다. 다시 입력하세요.")

        conn.close()

if __name__ == "__main__":
    main()