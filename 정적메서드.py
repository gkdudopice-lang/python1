# 정적 메서드: 클래스나 인스턴스와 독립적으로 동작하는 함수를 만들고 싶을 때 사용합니다.
# @staticmethod 데코레이션을 사용하며, 인자로 self를 사용하지 않습니다.

class Car:
    isinstance_count = 0

    # 초기화 함수
    def __init__(self, size, model):
        self.size = size
        self.model = model
        Car.isinstance_count = Car.isinstance_count + 1 # 클래스 변수 이용
        print(f'자동차 객체 생성 수: {Car.isinstance_count}')

    def move(self, speed):
        self.speed = speed
        print(f'자동차 {self.size} & {self.model}가 시속 {self.speed}로 달립니다.')

    @classmethod
    def print_cnt(cls):
        print(f'자동차가 {cls.isinstance_count} 대 만들어 졌습니다.')

    @staticmethod
    def check_type(code):
        if(code <= 10): print('전기차 입니다.')
        elif(code <= 20): print('가솔린차 입니다.')
        elif(code <= 30): print('디젤차 입니다.')
        else: print('분류 코드가 없습니다.')

car1 = Car('소형', '모닝')
car2 = Car('중형', '소나타')
Car.print_cnt()

car1.move(90)
Car.check_type(11)
car2.move(70)











