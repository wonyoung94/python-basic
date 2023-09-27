# 받아쓰기 한다는 마음으로 쓰지 마라
# 코드의 의미를 알고 쳐라, 무턱대고 따라 쓴다고 하지 마라.
# apple / Apple 대소문자 구분을 한다.
# git add. / git add . 띄어쓰기 구분을 한다.
# message / massage 오타에 대한 실수가 잦으니 주의한다.
# 컨트롤 + / 하면 주석처리가 가능하다.

# 저장 변수, variable
# 1. 숫자(int)
dust = 10
# 2. 글자(sting)
dust = '5'
# 3. 참/거짓(boolean)
dust = True # False

# 변수들을 모아 데이터를 나열한 형식
# 1. 리스트 : 순서가 있는 데이터를 나열할 때 이용
dust_list = [10, 20, 30]
# 2. 딕셔너리 : 순서가 없는 데이터를 나열할 때 이용
dust_dict = {
    '서울': 100,
    '대전': 10,
    '부산': 50,
}

# 조건

age = 10
# if age > 20:
#     print('성인입니다.')
# elif age > 8:
#     print('청소년입니다.')
# else: 
#     print('어린이입니다.')

dust = 100
# if dust > 150:
#     print('매우나쁨')
# elif dust > 80:
#     print('나쁨')
# elif dust > 30:
#     print('보통')
# else:
#     print('좋음')
#이렇게 했을 때 동일하게 진행은 가능하지만, 가독성이 떨어짐
    
# if 150 <= dust:
#     print('매우나쁨')
# elif 80 <= dust < 150:
#     print('나쁨')
# elif 30 <= dust and dust < 79:
#     print('보통')
# else:
#     print('좋음')


# 반복
menus = ['짜장면','마라탕','샌드위치','와진짜뭐먹지']

# n=0
# while n < 4:
#     print(menus[n])
#     n = n + 1
# 인덱스 접근을 해야 할 경우에는 while 구문으로 작성

# for menu in menus: 
#     print(menu)
# 대부분의 반복은 for 문으로 작성