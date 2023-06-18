# 중복 if문

# a = int(input("점수 입력 : "))
# if a>=60:
#     print("합격")
# else:
#     print("불합격")

# 중복 if문

# a = int(input("점수입력 : "))
# if a>=80:
#     print("상")
# else:
#     if a>=60:
#         print("중")
#     else:
#         print("하")

# 기본 if문

# a = int(input("점수입력 : "))
# if a>=80:
#     print("상")
# elif a>=60:
#     print("중")
# elif a<60:
#     print("하")



# a = int(input("접수를 입력하세요 : "))

# if a>=90:
#     print("A")
# else:
#     if a>80:
#         print("B")
#     else:
#         if a>=70:
#             print("C")
#         else:
#             if a>=60:
#                 print("D")
#             else:
#                 print("F")

# print("학점입니다.")


# a = int(input("접수를 입력하세요 : "))

# if a>=90:
#     print("A")
# elif a>80:
#     print("B")
# elif a>=70:
#     print("C")
# elif a>=60:
#     print("D")
# else:
#     print("F")

# print("학점입니다.")


mon = int(input("월 : "))

if 1<=mon<=12:
    if 3<=mon<=5:
        print("%d월은 봄입니다" % mon)
    elif 6<=mon<=8:
        print("%d월은 여름입니다" % mon)
    elif 9<=mon<=11:
        print("%d월은 가을입니다" % mon)
    else:
        print("%d월은 겨울입니다" % mon)
else:
    print("입력이 바르지 않습니다.")