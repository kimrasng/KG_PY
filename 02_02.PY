# 변수 선언(초기화)

boolVar = True  # bool행 기본데이터
intVar = 0  # int행 기본데이터
floatVar = 0.0  # float 기본데이터
strVar = "" # string형 기본데이터

# 변수의 선언
# 변수는 어떠한 값을 저장하는 메모리 공간(그릇)
# 변수 선언은 그릇을 준비하는 것
# 파이썬은 C/C++, 자바 등과는 달리 변수를 선언하지 않아도 되지만 긴 코드를 작성할때는 사용될 면수를 미리 계획적으로 준비하는 것이 더 효율적이다.
# type() 타입함수 : 5호(데이터형을 알고자 할때)

type(boolVar)

type(intVar)

type(floatVar)

type(strVar)

# type() 함수를 사용하면 변수가 bool(불형), int)(정수), float(실수), str(문자열)형으로 생성된 것을 확인할 수 있음
# 변수명 규칙
# 대 - 소문자를 구분한다 (예 myVar와 MyVar는 다른 변수). 문자, 숫자, 언더바(_)를 포함할 수 있다.
# 하지만 숫자로 시작함녀 안 된다(예 var2(0), _var(0), var_2(0), 2Var(X)).
# 예약어는 변수명으로 쓰면 안된다. 파이썬의 예약어는 True, False, None, and, ot, not, break, continue, return, if, elif, for, while, except, finally, gloval, import, try 등이다.

boolVar = False

intVar = 100

floatVar = 123.45

strVar = "안녕"

boolVar, intVar, floatVar, strVar
# 변수는 값을 담으면(대입하면) 사용가능, 변수에 있던 기존 값은 없어지고 새로 입력한 값으로 변경됨
var2 = 200
var1 = var2
var1

# 변수에는 변수의 값을 넣을 수도 있고, 계산 결과를 넣을 수도 있다.

var1 = var2+100
var1

# 변수에는 수샂와 변수의 연산을 넣을 수도 있음

var1 = var2 = var3 = var4 = 100
var1

# 변수는 연속된 값을 넣을수 있다 (맨 뒤에서 부터 대입)
var1 = var1 + 200
var1

# 변수에 연산 결과를 자신의 값으로 다시 대입하는 방식

myVar = 100

type(myVar)

# 파이썬에서 변수의 데이터 형식은 값을 넣는 순간마다 변경될 수 있는 유연한 구조
# myVar의 데이터형이 정수형에서 실수형으로 변경됨

# 10 = 100

#에러. 10이 상수이기 때문에
# 대입 연산자(=)의 왼쪽에는 무조건 변수만 올 수 있고, 오른쪽에는 무엇이든(값, 변수, 수식, 함수 등) 올 수 있음