from simple_colors import *   # 화면 출력시 컬러 지원
import threading  # 쓰레드 기능을 사용하기 위함
import time   # sleep() 사용을 위해
import random

# 상속을 주기 위한 유닛
class Unit:
    def __init__(self, pp, mp, ph, mh, hp):
        self.p_power = pp
        self.m_power = mp
        self.p_hit = ph
        self.m_hit = mh
        self.hp = hp
        self.alive = True  # 생사 여부

    def set_damage(self, damage):  # 피해를 받는 정도
        if self.hp > damage: # 체력이 더 큰 경우
            self.hp -= damage  # 데미지를 받은 만큼 체력을 감소 시킴
            self.alive = True
        else:
            self.hp = 0
            self.alive = False

    def is_alive(self):   # 생존 여부를 확인하는 메서드
        return self.alive

# Unit을 상속 받아 캐릭터 생성하기
class Character(Unit):
    def __init__(self, pp, mp, ph, mh, hp, um, job):  # 자식 생성자
        super().__init__(pp, mp, ph, mh, hp)  # 부모의 생성자 호출
        self.ultimate = um   # 궁극기 추가
        self.job = job  # 직업 추가

    # 물리 공격
    def p_attack(self):
        return self.p_power * self.p_hit

    # 마법 공격
    def m_attack(self):
        return self.m_power * self.m_hit

    # 궁극기
    def attack_ultra(self):
        return self.ultimate

# 결과 출력 함수
def print_status(character):
    if character.is_alive():
        print(f"남아 있는 {green(character.job)}의 체력은 {blue(f'{character.hp:.2f}')}입니다.")
    else:
        print(f"{green(character.job)}가 죽었습니다. 게임을 종료 합니다.")

def perform_attack(attacker, defender):
    val = random.choice(["physical", "magical"]) # 물리/마법 중 렌덤
    ul = random.randint(1, 18)  # 1 ~ 18 사이의 임의값 생성

    if val == "physical":
        damage = attacker.p_attack()
        print(f"{blue('물리공격')} >> {defender.job}에게 {yellow(f'{damage:.2f}')}데미지 입힘")
    else:
        damage = attacker.m_attack()
        print(f"{yellow('마법공격')} >> {defender.job}에게 {yellow(f'{damage:.2f}')}데미지 입힘")

    defender.set_damage(damage)
    print_status(defender)

    if ul == 1: # 1 ~ 18까지의 임의의 수에서 1인 경우 이므로 18분의 1의 확률
        damage = attacker.attack_ultra()
        print(f"{red('궁극기 발동')} >> {defender.job}에게 {red(f'{damage:.2f}')}데미지 입힘")
        defender.set_damage(damage)
        print_status(defender)

# 동작할 쓰레드 함수 만들기
def wizard_thread():
    print(f"{wizard.job}가 전투 준비를 완료 했습니다.")
    time.sleep(1)  # 1초 대기
    while True:
        time.sleep(5)
        if not warrior.is_alive() or not wizard.is_alive(): break
        perform_attack(wizard, warrior)


# 스레드 분리 후 두개의 캐릭터가 동시 동작 하도록 구현
# 메인 영역
if __name__ == "__main__":
    name1 = input("전사 이름 만들기 : ")
    name2 = input("마법사 이름 만들기 : ")
    warrior = Character(8, 2, 0.8, 0.5, 150, 40, name1)
    wizard = Character(2, 20, 0.5, 0.9, 60, 55, name2)

    x = threading.Thread(target=wizard_thread)  # 쓰레드 생성 및 실행할 함수 등록
    print(f"{warrior.job}가 전투 준비를 완료 했습니다.")
    time.sleep(1)
    x.start()  # 서브 스레드 시작
    while True:
        time.sleep(5)
        if not warrior.is_alive() or not wizard.is_alive(): break
        perform_attack(warrior, wizard)

