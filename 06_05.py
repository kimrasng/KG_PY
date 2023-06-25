# singer = {}

# singer['이름'] = '트와이스'
# singer['구성원수'] = 9
# singer['데뷔'] = '서바이벌 식스틴'
# singer['대표곡'] = 'SIGNAL'

# for k in ['학번', '이름', '학과']:
#     print('%s ---> %s' % (k, singer[k]))

foods = {"떡뽁이":"오댕",
         "짜장면":"단무지",
         "라면":"김치",
         "피자":"피클",
         "맥주":"땅콩",
         "치킨":"치킨무",
         "삼겹살":"상추"};

while(True):    # 무한 반반복
    myfood=input(str(list(foods.keys())) + "중 좋아하는 음식은?")   # 딕셔너리의 키 목록 출력
    if myfood in foods: # 탈출 while문 입력한 음식이 딕셔너리에 있으면 아래행 출력
        print("<%s> 궁합 음식은 <%s>입니다." % (myfood, foods.get(myfood)))
    elif myfood == "끝":    # '끝' 입력하면 무한반복 빠져나감
        break
    else:   # 모두 해당되지 않으면 아래 메시지 출력
        print("그런 음식이 없음니다. 확인해 보세요")
    