from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
import csv
import random

#반복문 돌릴 식당 리스트
#restaurantlist = ['문득','나인온스버거','오막회집','오지편한식당','용마커피','쥬벤쿠바','맨프롬오키나와',
#                   '메이드바이아린''옷살','모다모다','시골집','몽중인','카페프레임','제주상회',
#                    '더멜팅팟','토끼네마굿간','모단걸응접실','도리도리하찌','아띠85도씨',
#                    '순보보','코코미','미각담다','오늘그대와','까까','우리가참순대','혼네',
#                    '펭귄제과','쟝블랑제리','아모르미오','미미청','쿠모식당','미드레벨','소블리',
#                   '프로젝트서울','카페미엘','동네아저씨치킨','황토방',]

#notworking = ['라티놀','더고기','성민양꼬치2호점','빽돈본점',]

# restaurantlist = ['송원숯불갈비','이태리파파','육회포차','사운드마인드','우동요츠야',
#                   '땅콩카페','커피볶는여자','진주상회','호타루','쭈앤쭈','새우당','너구리덮밥','봉천예술관']
# restaurantlist = ['티라노커피','샤로스톤','면화당','삼차','스시스캔들','엘따뻬오','와인창고잡']
# restaurantlist = ['씨앗양식','기절초풍왕순대','다이조부','히토리더야끼니꾸','방콕야시장','로향양꼬치','소풍가는날',
#                '딸랏롯빠이','피기스페이보릿','원초족본능','오드비','나에게오는길','사케바히토리','새실정원',
# '쁘띠크','오른손푸드카페','차이나당','서울대곱창','대중주점','모던보이작업실','막걸리카페잡','바닐라스카이']
# restaurantlist = ['도깨비포차','현씨공방','참새방앗간','외래향']
# restaurantlist = ['오인자아구찜','샤로수흑돈','엔조','연탄부락','엉클비','정박사','고기야','뉴욕인진바','나는남자닭', 
#                 # '아비정전','소우주','카페블리스','제리','만화경','김창일스시','한우육회마을','깐족깐족','딱좋아']
# restaurantlist = ['미스리부자아줌마','스월링','사시사철흑염소오리','낙성기사식당','화상손만두','무삥과팟타이', 
#             '이상범스시','정육식당솔','더은교','도모다찌','잇쇼쿠','엘리펀트키친','엘비스맥주','마담봉봉','온고지신','딱좋아',]
# restaurantlist = ['조선pub에디','프랑스홍합집','동경산책','텐동요츠야','오늘그대와',
#                     '진주상회','쭈앤쭈','새우당','너구리덮밥','봉천예술관','사케바히토리','고봉식당','사운드마인드',
# restaurantlist = ['우동요츠야','육회포차']
restaurantlist = ['샤로수길맛집']
#이 위에까지가 2년 이상 생존 추정인 식당들


#밑에부터는 2년 미만 추정인 곳들
# restaurantlist = ['데일리오아시스', '섭지수산','키요이''오신매운갈비찜','남도반주','충청삼겹','하울링데이즈',
                    # '테일러슬라이스피자','안녕와인','아로이팟타이','다르빛두번째이야기','백산식당','달첨시루','옐로우버터드림','누들히우스']
#twounder = [,
# '구이닭연구소','트라토리아체나','잔잔','샤이케멘','엄지오뎅','호랑이면','육감소감','달곱','책술음악',
# '카페플러피','알뜰수산','아나타노로바다야끼','삼미제면','앙뿌','산이형회포차','모리돈부리','맥주는별책부록',
# '십장생베이커리','수이','슬리핑피쉬','소문난집','연소바','황칠나라풍년옥','두근두근쭈꾸미','소디스펍',
# '미족원','일품낙성불백','낙성대우동','라화쿵부마라탕','어멍',]

baseurl = 'https://www.instagram.com/'
# plusurl = input('검색할 태그를 입력하세요: ')
#url = baseurl + quote_plus(plusurl)
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88'}


# driver = webdriver.Chrome('chromedriver',options=options)
driver = webdriver.Chrome()
driver.get(baseurl)

time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')



#로그인
# loginbutton = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button'
# driver.find_element_by_xpath(loginbutton).click()

time.sleep(random.uniform(1,3))

# email = '비밀'
email = '비밀'
elem_login = driver.find_element_by_name('username')
elem_login.clear()
elem_login.send_keys(email)

time.sleep(random.uniform(1,2))

# passwordd = '비밀'
passwordd = '비밀'
elem_login = driver.find_element_by_name('password')
elem_login.clear()
elem_login.send_keys(passwordd)

xpath = '//*[@id="loginForm"]/div/div[3]/button'
driver.find_element_by_xpath(xpath).click()

time.sleep(random.uniform(4,6))

#로그인정보 저장 나중에하기
xpath1 = '//*[@id="react-root"]/section/main/div/div/div/div/button'
driver.find_element_by_xpath(xpath1).click()

time.sleep(random.uniform(2,4))

#알림설정 나중에하기
# xpath4 = '/html/body/div[4]/div/div/div/div[3]/button[2]'
# driver.find_element_by_xpath(xpath4).click()

# time.sleep(random.uniform(1,3))

# xpath2 = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'
# findtab = driver.find_element_by_xpath(xpath2)
# findtab.clear()
# findtab.send_keys(plusurl)

time.sleep(random.uniform(2,4))

# hashtag = '#react-root > section > nav > div._8MQSOㅇ.Cx7Bp > div > div > div.LWmhU._0aCwM > div.drKGC > div > a > div > div > div.uyeeR'
# driver.find_element_by_css_selector(hashtag).click()

# time.sleep(3)

url_list=[]

for res in restaurantlist:
    url_list.append(baseurl+'explore/tags/'+quote_plus(res))
count = 0
for url in url_list:
    driver.get(url)
    time.sleep(random.uniform(4,6))
    html=driver.page_source
    soup=BeautifulSoup(html, 'html.parser')
    tagall=[]
    taglist = []
    #div.v1Nh3.kIKUG._bz0w

    time.sleep(random.uniform(2,4))
    posts = driver.find_element_by_css_selector('span.g47SY').text

    
    #몇 개의 게시글을 크롤링 할지 
    if ',' in posts:
        numberofcrawl = 10000
    elif int(posts) >= 300:
        numberofcrawl = 300
    elif int(posts) < 300:
        numberofcrawl = int(posts)

    # print(numberofcrawl)

    driver.find_element_by_css_selector('._9AhH0').click()
    for i in range(numberofcrawl):
        time.sleep(random.uniform(1,4))
        try:
            # 태그 종류
            data = driver.find_element_by_css_selector('.XQXOT.pXf-y') 
            tag_raw = data.text
            tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
            tag = ''.join(tags).replace("#"," ")
            tag_data = tag.split()
            for tag_one in tag_data:
                taglist.append(tag_one)
        except:
            taglist.append("error")
        try: 
            WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a._65Bje.coreSpriteRightPaginationArrow')))
            driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow').click()
        except:
            print('여기까지!')
            break

    time.sleep(1)
    print(taglist)
    # stop_words = ['f4f', 'l4l', '맞팔', '팔로우', '소통', '좋아요반사', '좋반', 'fff']
    stop_words=['error']
    tagall = [word for word in taglist if word not in stop_words]
    with open(f'{restaurantlist[count]}_{posts}중{str(numberofcrawl)}.csv', 'w', encoding='cp949', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(taglist)
    f.close()
    count += 1


driver.close()





# with open(f'{plusurl}_{posts}중{str(numberofcrawl)}.csv', 'w', encoding='cp949', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow('해시태그')
#     writer.writerows(tagall)


print('완료되었습니다!')
