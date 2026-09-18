# 상속: 부모 클래스에서 만든 변수와 메서드를 물려 받아 사용할 수 있음
# 오버라이딩: 부모 클래스의 매서드를 상속 받아 재정의 하는 것

class ProtoTV: # 상속을 주기 위한 부모 클래스
    pass
    # 전원, 채넣, 볼륨을 매개변수로 하는 생성자 생성
    def __init__(self, power=False, chnnel=7, volume=20):
        self.power = power
        self.chnnel = chnnel
        self.volume = volume

    # 전원을 켜고 끄는 매서드
    def set_power(self, power):
        self.power = power
        if self.power:
            print('전원이 켜졌습니다.')
        else:
            print('전원이 꺼졌습니다.')

    # 채널 설정 매서드 (1 ~ 1000) 사이
    def set_chnnel(self, chnnel):
        if self.power:
            if 1 <= self.chnnel <= 1000:
                self.chnnel = chnnel
                print(f'채널{chnnel}번으로 이동')
            else:
                print('(1 ~ 1000)번 사이만 가능합니다.')
        else:
            print('TV전원을 켜주세요.')

    # 볼륨 설정 메서드 (0 ~ 100) 사이
    def set_volume(self, volume):
        if self.power:
            if 0 <= self.volume <= 100:
                self.volume = volume
                print(f'볼륨이 {volume}으로 변경되었습니다.')
            else:
                print('(0 ~ 100)번 사이만 가능합니다.')
        else:
            print('TV전원을 켜주세요.')

class ProductTV(ProtoTV):
    def set_channel(self, channel): # 오버라이딩
        if 0 < channel < 2000:
            self.channel = channel
            print(f'채널 {channel}번으로 이동되었습니다.')
        else:
            print('(1 ~ 1000)번 사이만 가능합니다.')

    # 정보를 출력하는 메서드 만들기
    def display_info(self):
        if self.power:
            status = 'ON'
        else:
            status = 'OFF'
        print(f'ProductTV 현재상태: {status}')

        if self.power:
            print(f'볼륨 현재상태: {self.volume}')
            print(f'채널 현재상태: {self.chnnel}')

productTV = ProductTV(False, 10, 10)
productTV.set_power(True)
productTV.set_channel(1200)
productTV.set_volume(40)
productTV.display_info()






