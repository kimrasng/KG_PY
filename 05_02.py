# 문제 : 컴퓨터의 숫자의 짝수, 홀수를 판별하는 프로그램
# 컴퓨터 발생한 난수(변수 : N 숫자의 법위는 10~99)
# 사용자 판단한 홀 짝(변수 : user)
# import random

# N = random.randint(10, 99)
# user = int(input("홀(0) 또는 짝(1또는 0이외의 모든 정수)을 입력하세요 :"))
# if N % 2 == 0:
#     if user == 0:
#         print("틀렸습니다.")
#     else:
#         print("맞았습니다")
# else:
#     if user == 0:
#         print("맞았습니다")
#     else:
#         print("틀렸습니다")
# print("컴퓨터의 숫자는 %입니다." % N)



# 컴퓨터의 숫자의 짝수, 홀수를 판별하는 게임 프로그램 무한 반복으로 (아래 결과와 같이 출력)
# 컴퓨터 발생한 난수 (변수 : N 숫자의 범위는 10~99)
# 사용자 판단한 홀 짝(변수 :user)
# life (목숨변수 : -1), score(점수 : 100)
import random
import os
import time

life = 5
score = 0

while True:
    if life == 0:
        print("Game Over")
        break

    N = random.randint(10, 99)
    
    print("현재 목숨", life, "현재 점수", score)
    user = int(input("홀(0) 또는 짝(1또는 0이외의 모든 정수)을 입력하세요 :"))
    if N % 2 == 0:
        if user == 0:
            life -= 1
            print("틀렸습니다.")
        else:
            life += 100
            print("맞았습니다")
    else:
        if user == 0:
            life += 100
            print("맞았습니다")
        else:
            life -= 1
            print("틀렸습니다")
    print("컴퓨터의 숫자는 %입니다." % N)
    # time.sleep(5)   # time.sleep(초) 일시정지
    #os.system('cls')   # 시스템 종료

print("총점수 : %d" % score)