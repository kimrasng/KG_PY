aa = [10, 20, 30, 40, 50]
aa[0]



# 리스트 코드와 비교 : 리스크는 대괄호[]로 묶고 문자열은 작은따옴표로 묶어 출력

ss = '파이선'+'최고'
ss

ss = '파이썬'*3
ss

ss='파이썬abcd'
ss
len(ss)
# len() 함수 : 리스트나 문자열의 개수를 셀 때 사용

SS = "Python is Easy. 그래서 progrmming이 재미있습니다.^^"

ss.upper()
ss.lower()
ss.title()

ss = '파이썬 공부는 즐겁습니다. 물론 모든공부가 다 재미있지는 않죠. ^^'
ss.count('공부')
ss.find('공부')
ss.rfind('공부')
ss.find('공부', 5)
ss.find('없다')
ss.index('공부')
ss.rindex('공부')
ss.index('공부', 5)
ss.index('없다')
ss.startswith('파이썬')
ss.startswith('파이썬',10)
ss.endswith('^^')

ss = '  파  이  썬  '
ss.strip()

ss.rstrip()

ss.lstrip()

ss = '-----파----이----썬'
ss.strip('-')
ss.rsplit('-')
ss.lstrip('-')
ss = '<<<<파<<<이>>>>썬>>>>'
ss.strip('<>')
ss.rsplit('<>')
ss.lstrip('<>')