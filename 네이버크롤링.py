import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time
import os


def crawl_stock_data(code: str) -> dict:
    """
    네이버 금융에서 종목 코드를 받아 주식 정보를 스크래핑하는 함수

    Args:
        code (str): 종목 코드 (예: "005930")

    Returns:
        dict: 종목명, 종목코드, 현재가, 거래량을 담은 딕셔너리. 실패 시 None.
    """
    try:
        url = f"https://finance.naver.com/item/main.naver?code={code}"
        # 네이버의 차단을 피하기 위한 User-Agent 설정
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()  # 오류 발생 시 예외 처리

        bs_obj = BeautifulSoup(res.text, "html.parser")

        # --- 데이터 추출 ---
        # 가격 정보
        div_today = bs_obj.find("div", {"class": "today"})
        if not div_today:
            print(f"[{code}] 가격 정보를 찾을 수 없습니다.")
            return None
        price = div_today.find("em").find("span", {"class": "blind"}).text

        # 회사 정보 (이름, 코드)
        h_company = bs_obj.find("div", {"class": "h_company"})
        if not h_company:
            print(f"[{code}] 회사 정보를 찾을 수 없습니다.")
            return None
        name = h_company.a.text
        code_in_page = h_company.find("div", {"class": "description"}).span.text

        # 거래량 정보
        table_no_info = bs_obj.find("table", {"class": "no_info"})
        if not table_no_info or len(table_no_info.tr.find_all("td")) < 3:
            print(f"[{code}] 거래량 정보를 찾을 수 없습니다.")
            volume = "N/A"
        else:
            volume = table_no_info.tr.find_all("td")[2].find("span", {"class": "blind"}).text

        return {
            "종목명": name,
            "종목코드": code_in_page,
            "현재가": price,
            "거래량": volume
        }
    except requests.exceptions.RequestException as e:
        print(f"[{code}] 요청 중 오류 발생: {e}")
        return None
    except Exception as e:
        print(f"[{code}] 데이터 처리 중 오류 발생: {e}")
        return None


def run_scraping_job():
    """
    지정된 종목들의 데이터를 수집하여 엑셀 파일로 저장하는 메인 작업 함수
    """
    # 요청하신 종목 코드 리스트
    codes = ["005930", "005380", "000270", "000720", "035720", "042660", "012330", "066570"]

    results = []

    print(f"--- {time.ctime()} | 데이터 수집 시작 ---")
    for code in codes:
        data = crawl_stock_data(code)
        if data:
            results.append(data)
            print(f"  - {data['종목명']}({data['종목코드']}) 수집 완료")
        else:
            print(f"  - {code} 수집 실패")
        time.sleep(1)  # 서버에 부담을 주지 않기 위해 잠시 대기

    if not results:
        print("수집된 데이터가 없어 파일을 저장하지 않습니다.")
        return

    # pandas DataFrame으로 변환
    df = pd.DataFrame(results)

    # 엑셀 파일로 저장
    output_filename = "stock_prices.xlsx"
    df.to_excel(output_filename, index=False, engine='openpyxl')

    print(f"--- {time.ctime()} | 데이터 수집 및 엑셀 저장 완료 ---")
    print(f"결과가 '{os.path.abspath(output_filename)}' 파일에 저장되었습니다.")


if __name__ == '__main__':
    # --- 즉시 1회 실행 ---
    run_scraping_job()

    # --- 스케줄링 실행 ---
    # 매일 오전 9시 30분에 작업 실행하도록 설정
    schedule.every().day.at("11:03").do(run_scraping_job)

    # # 10분마다 실행 (테스트용)
    # schedule.every(10).minutes.do(run_scraping_job)

    print("\n스케줄러가 시작되었습니다. 매일 09:30에 작업을 수행합니다.")
    print("프로그램을 종료하려면 Ctrl+C를 누르세요.")

    while True:
        schedule.run_pending()
        time.sleep(1)

















