# 에어컨 만들기
# - 전원 : ON / OFF
# - 현재 온도 표시 기능 (기본값은 20도)
# - 온도 설정 기능 (1도씩 설정 가능)
# - 바람 세기 설정 : 1단계, 2단계, 3단계

class Aircon:
    # 전원, 설정온도, 바람 세기를 매개변수로 전달 받은 생성자 만들기
    def __init__(self, name, power=False, temperature=20, wind_speed=1):
        self.name = name
        self.power = power
        self.temperature = temperature
        self.wind_speed = wind_speed

    # 전원 ON/OFF
    def set_power(self, power):
        self.power = power
        if self.power:
            print('에어컨이 켜졌습니다.')
        else:
            print('에어컨이 꺼졌습니다.')

    # 온도 설정
    def set_temperature(self, temperature):
        if self.power:
            self.temperature = temperature
            print(f'온도가 {temperature}도로 설정되었습니다.')
        else:
            print('에어컨 전원을 켜주세요.')

    # 바람 세기
    def set_wind_speed(self, wind_speed):
        if self.power: # 에어컨이 켜져 있고
            if 1 <= wind_speed <= 3: # 1~3단계 사이라면
                self.wind_speed = wind_speed # 실행하겠다
                print(f'바람 세기가 {wind_speed}단계로 설정 되었습니다.')
            else:
                print('1~3단계만 선택 가능합니다.')
        else:
            print('에어컨 전원을 켜주세요.')

    # 에어컨 정보 표시
    def display_info(self):
        if self.power == True:
            status = '켜짐'
        else:
            status = "꺼짐"

        print('-' * 30)
        print(f"현재 에어컨 상태: {status}")

        if self.power:
            print(f'설정 온도: {self.temperature}')
            print(f'바람 세기: {self.wind_speed}')
        print('-' * 30)

# 에어컨 객체 생성하고 메뉴를 구성해 동작 해보기
# 객체 생성
room_ac = Aircon('방 에어컨')
# 처음 상태 확인하기
room_ac.display_info()
# 전원 켜보기
room_ac.set_power(True)
# 온도랑 바람 세기 조절해보기
room_ac.set_temperature(22)
room_ac.set_wind_speed(3)
# 바뀐 상태 다시 확인하기
room_ac.display_info()
# 전원 꺼보기
room_ac.set_power(False)











