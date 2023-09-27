numbers = [1, 2, 3, 4, 5]
max_num = max (numbers)
# print(max_num)

#################
import random
random_number = random. randint(1,100)
# print(random_number)
#################

menus = ['치킨','피자','떡볶이']
random_number = random.randint(0,2)
# print(menus[random_number])

#메뉴에 각각 들어있는 항목에 넘버링을 한 후 랜덤 숫자를 추출, 그 숫자에 해당하는 메뉴를 출력
#최종 목표 : 메뉴 추천(메뉴 나열 - 라벨링 - 랜덤라벨 - 라벨 출력)

menu = random.choice(menus)
# print(menu)

#위의 메뉴 추천 시스템을 하나의 함수화

numbers = range(1, 46) # 1이상 46미만을 의미
lucky_number = random.sample(numbers, 6)
# print(lucky_number)
# print(sorted(lucky_number)) 
#sorted 함수로 정렬화
#로또 추첨 시스템 함수화

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086'

#terminal 창에서 pip install requests 입력해 설치 후 사용 가능
import requests
res = requests.get(URL)

# print(res)
#HTTP 상태코드 확인시 사용 : 200 일때 정상 

# print(res.text)
#받은 데이터의 텍스트 추출

data = res.json() 
#json 은 함수라서 ()가 필요하고 text 는 함수가 아님.
# print(data)
#텍스트를 data라는 변수로 딕셔너리 구조화

#원하는 데이터를 추출 가능
drwtNo1 = data['drwtNo1']
drwtNo2 = data['drwtNo2']
drwtNo3 = data['drwtNo3']
drwtNo4 = data['drwtNo4']
drwtNo5 = data['drwtNo5']
drwtNo6 = data['drwtNo6']

# print(drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6)
lotto_number = [drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6]

#당첨 번호만 추출
# print(data['drwNoDate'])
#당첨 날짜만 추출

#API란 : 
#JSON이란 : 

print(lucky_number)
print(lotto_number)

print(set(lucky_number) & set(lotto_number))
