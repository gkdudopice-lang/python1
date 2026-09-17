
class Television: # 클래스 이름은 대문자로 시작
    def __init__(self, name, on, channel, volume): # 인잇 = 생성자
        self.name = name
        self.is_on = on
        self.channel = channel
        self.volume = volume

    def set_on(self, on):
        self.is_on = on

    def set_channel(self, cnl):
        self.channel = cnl

    def set_volume(self, vol):
        if 0 <= vol <= 100:
            self.volume = vol
        else:
            print('볼륨값 입력 범위를 초과 했습니다.')

    def get_on(self):
        return self.is_on

    def get_channel(self):
        return self.channel

    def get_volume(self):
        return self.volume

    def view_tv(self):
        power = ('OFF', 'ON')
        print(f'이름: {self.name}')
        print(f'전원: {power[self.is_on]}')
        print(f'채널: {self.channel}')
        print(f'볼륨: {self.volume}')

lg_tv = Television('LG', False, 10, 10)
samung_tv = Television('SAMUNG', False, 20, 20)
samung_tv.view_tv()
lg_tv.view_tv()






