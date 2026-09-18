# 연산자 오버로딩은 내장 연사자를 사용자 정의 클래스에 대해 다르게 동작하도록 재정의 하는 것

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)

v3 = v1 + v2 # '+' 연산자가 __add__메서드를 호출합니다.
print(v3.x, v3.y) # 출력: 4,6

v5 = 10
v6 = 20
print(v5 + v6)

print(v1 == v2) # '=='연산자가 __eq__메서드를 호출합니다.