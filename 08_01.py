# class Car:
#     color = ""
#     speed = 0

#     def upSpeed(self, value):
#         self.speed += value
    
#     def downSpeed(self, value):
#         self.speed -= value

# myCar1 = Car()
# myCar1.color = "빨강"
# myCar1.speed = 0

# myCar2 = Car()
# myCar2.color = "파랑"
# myCar2.speed = 0

# myCar3 = Car()
# myCar3.color = "노랑"
# myCar3.speed = 0

# myCar1.upSpeed(30)
# print("자동차1의 색상은 %s이며, 현재 속도는 %dKM입니다." % (myCar1.color, myCar1.speed))

# myCar2.upSpeed(60)
# print("자동차1의 색상은 %s이며, 현재 속도는 %dKM입니다." % (myCar2.color, myCar2.speed))

# myCar3.upSpeed(0)
# print("자동차1의 색상은 %s이며, 현재 속도는 %dKM입니다." % (myCar3.color, myCar3.speed))


# # 클래스의 개념
# # 클래스의 모양과 생성

# # class 클래스명:
#     # 이 부분에 관련 코드 구형

# # 현실 세계의 시물을 커퓨터 안에서 구현하려고 고안된 개념

# # 자동차를 클래스로 구현

# # 자동차 클래스의 개념을 실제 코드로 구현
#     # 자동차의 속성은 지금까지 사용한 변수처럼 생성(필드( Field ))
#     # 자동차의 기능은 지금까지 사용한 함수 형식으로 구현
#     # 클래스 안에서 구현된 함수라고 하지 않고 메서드라고 함.

# # 클래스 사용순서
#     # 1단계 (클래스선언)
#     # 2단계 (인스턴스 생성)
#     # 3단계 (필드나 메서드 사용)




# # 매개변수가 self만 있는경우
# class Car:
#     color = ""
#     speed = 0

#     def __init__(self): # 인스턴트생성 행에서 자동으로 값 초기호
#         self.color = "빨강"
#         self.speed = 0

#     def upSpeed(self, value):
#         self.speed += value
    
#     def downSpeed(self, value):
#         self.speed -= value

# myCar1 = Car()
# myCar1.color = "빨강"
# myCar1.speed = 0

# myCar2 = Car()
# myCar2.color = "파랑"
# myCar2.speed = 0

# myCar3 = Car()
# myCar3.color = "노랑"
# myCar3.speed = 0

# myCar1.upSpeed(30)
# print("자동차1의 색상은 %s이며, 현재 속도는 %dKM입니다." % (myCar1.color, myCar1.speed))

# myCar2.upSpeed(60)
# print("자동차1의 색상은 %s이며, 현재 속도는 %dKM입니다." % (myCar2.color, myCar2.speed))

# # 생성자의 개념 : 인스턴스를 생성하면서 필드값을 초기화시키는 함수
# # 생성자의 기본
# # 생성자의 기본 형태 : __init__( ) 라는 이름
# # TIP : __init__( )는 앞뒤에 언더바(_)가 2개씩. init는 Initialize의 약자로 초기화 의미
#     # 언더바가 2개 붙은 것은 파이썬에서 예약해서 놓은 것, 프로그램을 작성시 이 이름을 사용해서 새로운 함수나 변수명을 만들지 말 것





# # 매개변수가 있는 생성자
# class Car:
#     color = ""
#     speed = 0

#     def __init__(self, value1, value2): # 생성자에서 매개변수 2개를 받도록 설정
#         self.color = value1
#         self.speed = value2

#     def upSpeed(self, value):
#         self.speed += value
    
#     def downSpeed(self, value):
#         self.speed -= value

# myCar1 = Car("빨강, 30")
# myCar2 = Car("파랑, 60")

# print("자동차1의 색상은 %s이며, 현재 속도는 %dKM입니다." % (myCar1.color, myCar1.speed))
# print("자동차2의 색상은 %s이며, 현재 속도는 %dKM입니다." % (myCar2.color, myCar2.speed))



# class Car:
#     color = ""  # 인스턴트 변수
#     speed = 0   # 인스턴스 변수
#     count = 0   # 클래스 변수 count 를 선언하고 0으로 초기화

#     def __init__(self): # 생성자 안에서 클래스 변수에 접근하려고 클래스명. count 를 1증가
#         self.color = 0
#         self.speed += 1

#     def upSpeed(self, value):
#         self.speed += value
    
#     def downSpeed(self, value):
#         self.speed -= value

#     myCar1, myCar2 = None, None


# myCar1 = Car()
# myCar1.speed = 30
# print("자동차1의 현재 속도는 %dkm이며, 생산된 자동차는 총 %d대입니다." % (myCar1.speed, Car.count))

# myCar2 = Car()
# myCar2.speed = 30
# print("자동차2의 현재 속도는 %dkm이며, 생산된 자동차는 총 %d대입니다." % (myCar2.speed, Car.count))

# # 클래스 변수
# # 클래스 안에 공간이 할당된 변수, 여러 인스턴스가 클래스 변수 공간 함께사용



class Car:
    speed = 0
    def upSpeed(self, value):
        self.speed += value
        print("현재속도(슈퍼클래스): %d" % self.speed)

        if self.speed>150:  # 서브 클래스 (sedan)의 supSpeed()메서드 다시 만듬(메서드 오버라이딩)
            self.speed = 150
        print("현제 속도(서브클래스): %d" % self.speed) # 서브 클래스 (truck)에는 아무런 내용 없어 슈퍼 클래스(car)의 메서드를 그대로 상속

class Truck(Car):
    pass

sedan, truck = None, None

truck1 = Truck()
sedan1 = Sedan()

print("트럭 -->", end="")   # Truck인스턴스의 upSpeed () 호출하면 슈퍼 클래스 (car)의 upSpeed() 메서드 호출
truck1.upSpeed(200)

print("승용차 -->", end="") # Sedan 인스턴스의 upSpeed () 메서드 호출하면 재정의된 upSpeed(메서드 호출)
sedan1.upspeed(200)ㅋ

# 상속의 개념
    # 공통된 내용을 자동차 클래스에 두고 상소을 받음으로써 일관되고 효율적인 프로그래밍 가능
    # 상위 클래스인 자동차 클래스를 슈퍼 클래스 또는 부모 클래스, 하위의 승용차와 트럭 클래스는 서브 클래스 또는 자식 클래스
# 메서드 오버라이딩
    # 사우이 클래스의 메서드를 서브 클래스에서 재정의