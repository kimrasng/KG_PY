# a = 90
# if a<100:
#     print("100보다 작군요")

'''
if 조건식:  # 조건식이 참일때 아래문장이 실행
    실행문장
'''
sel = int(input("입력진수 결정(16/10/8/2)"))    # 진수 결정
num = input("값 입력 : ")   # 문자 값을 num에 입력

if sel == 16:
    num10 = int(num, 16)

if sel == 10:
    num10 = int(num, 10)

if sel == 8:    # 8진수 num을 10진수로 변환하라
    num10 = int(num, 8)

if sel == 2:    # 2진수 num을 10진수로 변환하라
    num10 = int(num, 2)

print("16진수 ===> ", hex(num10))   # 십진수 num 10의 값을 16진수로 변환하라
print("10진수 ===> ", num10)   # 십진수 num 10의 값을 10진수로 변환하라
print("8진수 ===> ", oct(num10))   # 십진수 num 10의 값을 8진수로 변환하라
print("8진수 ===> ", bin(num10))   # 십진수 num 10의 값을 8진수로 변환하라
