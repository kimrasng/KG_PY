# 문자열이 모든 글자 뒤에 $를 붙여서 출력하는 코드
# ss = '파이썬짱!'

# sslen = len(ss) # 문자열의 길이 를sslen변수에 저장
# for i in range(0, sslen):   # 문자열의 길이만큼 반복
#     print(ss[i] + '$', end='')  # 글자 하나와 $를 붙여서 출력


# 문자열을 입력하세요 반대로 출력

# instr, outstr = '',''
# count, i = 0, 0

# instr = input("문자열을 입력하세요 : ")
# count = len(instr)

# for i in range(0, count):   # 문자열의 개수만큼 반복.
#     outstr = outstr+instr[count-(i+1)]
# # 입력한 문자열이 3글자라면 instr[0], instr[1], instr[2] 3개가 있는 것이므로
# # 첫 번째(i가 0)에는 instr[2]가 추가, 두번째 (i가 1) 에는 instr[1]이 추가 세번째 (i가2)에는 instr[0]에추가
# print("내용을 거꾸러 출력 ==> %s" % outstr) # 거꾸로 돌린 문자열 출력

# 문자열이 괄호로 감싸 있지 않으면 괄호로 감싸 주는프로그램
# ss = input("입력 문자열 ==>", end="")
# print("출력문자열 ==>", end="")

# if ss.startswitch('()')==False:
#     print("(", end='')

# if ss.endswitch(')')==False:
#     print(ss,end="")


# 입력 문자열 ==> 파이썬은 재미있다
# 출력 문자열 ==> (파이썬은 재미있다.)



# 문자열 양옆에 [] 넣은 후 문자열 중간 중간의 공백까지 상제해 주는 코드

# 원래 문자열 ==> [   한글 Python프로그래밍   ]
# 공백 삭제 문자열 ==> [한글 Python프로그래밍]

# inStr = "   한글 Python프로그래밍   "
# outStr = ""

# for i in range(0, len(inStr))
#     if inStr[i] != '    ':  # 공백이 아니면 이어서 출력하고 공백이면 건너뜀
#         outStr += outStr[i] # 다음 문자를 이어서 출력
# print("원래 문자열 ==>"+'['+inStr+']')



# 문자열을 입력받아 그중 o을 $로 변경하는 문자열 변경를 응용

# ss = input("입력 문자열 ==>")

# print("출력문자열 ==>", end = '')

# for i in range(0, len(ss)):
#     if ss[i] !='o':
#         print(ss[i], end='')
#     else:
#         print('$', end="")



# 연/월/일 형식으로 문 // 날짜 (연/월/일)입력 ==> 2023/03/26
# 날짜 (연/월/일)입력 ==> 2023/06/25
# 입력한 날짜의 10년후 ==> 2033/06/25

ss = input("날짜(연/월/일) 입력==>")

ssList = ss.split('/')  # 입력한 문자열을 /로 리스트 값으로 불리 따라서 ssList에 ['2023', '03', '26;] 형식으로 분리
print("입력한 날짜의 10년후 ==>", end=' ')  # 연도를 가르키는 문자열인 SSlist[0](이 코드에서는 '2023')을 먼저 int()함수를 사용해
# 그리고 다시 str()함수로 문자열로 변경한 '2023'를 '년' 글자와 연결
print(str(int(ssList[0])+10)+"년", end = '')
print(ssList[1]+"월", end = '')
print(ssList[2]+"일")