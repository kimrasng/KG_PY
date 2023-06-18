# for문 반복

# for i in range(0, 3, 1):
#     print("안녕하세요")


# while 반복

# i = 0

# while i<3:
#     print("안녕하세요")
#     i = i+i


# 변수 = 시작값

# while 조건식:
#     실행문
#     증가값

# for 문으로 작성한 1에서 10까지의 합계 구하기 (while문으로)

# hpa = 0
# i = 1   # i의 시작 값을 1로 지정

# while(i<=11):   # i가 11보다 작으면 참, i가 10일 때까지 아래행 반복
#     hap = hpa + i   # hap에 i값(처음에는 1)을 누적
#     i = i + 1   # i를 1증가
# print("1ㅔ서 10까지 의 합 : %d" % hap)

# while True:
#     print("Z", end="")

hap = 0
a, b, = 0, 0

while True:
    a = int(input("더할 첫번째 수를 입력하세요 : "))
    b = int(input("더할 두번째 수를 입력하세요 : "))

    hap = a + b
    print("%d + %d = %d" % (a, b, hap))


# 무한 루푸를 하는 while문
    # 무한 루프 적용: 'while 조건삭 :'에 들어가는 조건식을 True로 지정

# 사용자가 Ctrl + C를 누룰 때까지 덧셈, 뺄셈, 곱셈, 나눗셈, 나머지까지 계산


while True:
    a = int(input("더할 첫 번째 수를 입력하세요 : "))
    b = int(input("더할 두 번째 수를 입력하세요 : "))
    ch = int(input("더할 연산자를 입력하세요 : "))

    if(ch == '+'):
        print("%d + %d = %d" % (a, ch, a+b))
    elif(ch == '-'):
        print("%d - %d = %d" % (a, ch, a-b))
    elif(ch == '*'):
        print("%d  %d = %d" % (a, ch, a*b))
    elif(ch == '/'):
        print("%d / %d = %d" % (a, ch, a/b))
    elif(ch == '%'):
        print("%d % %d = %d" % (a, ch, a%b))
    elif(ch == '//'):
        print("%d + %d = %d" % (a, ch, a//b))
    elif(ch == '**'):
       print("%d + %d = %d" % (a, ch, a**b))
    else:
        print("연산자를 잘못 입력했습니다.")