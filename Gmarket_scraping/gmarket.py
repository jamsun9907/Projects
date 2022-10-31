# G Market scrapper

# URL <region 이동은 xpath>
URL_SG = 'http://gcorner.gmarket.co.kr/Bestsellers/Country/SG'

# Today's Date
import datetime
today = datetime.date.today()

# 오늘의 파일 생성
file_name = str(today)+'_Scraper_Dataset_Gmarket.csv' #주의 실제 시작 후에는 write으로 하면 큰일남(내 소중한 데이터 없어짐)
Market = ['Singapore','Malaysia(West)','Taiwan']
header = ["Date","Local Market","Rank","Product name","Seller_name","Company","BRN","contact","email","URL"]

#csv 생성
import csv

with open(file_name,'w',newline='', encoding='cp949') as f:#cp949로 해야 한글 안깨짐
    writer = csv.writer(f)
    writer.writerow(header)

#사이트 접속
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

s = Service('/Users/sunyoung.jang/PycharmProjects/pythonProject/chromedriver')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(time_to_wait=5) #암묵적 대기


#######이제부터 SG 스크래핑을 시작하지
driver.get(URL_SG) #SG 웹사이트 열기

#오늘의 랭크 확인
rank_today = driver.find_elements(by=By.CSS_SELECTOR,value='span.rank')
end_rank = rank_today[-1].text
end_rank = int(end_rank)
print("오늘의 순위",end_rank,"위 까지")

def row_maker(n):
    from selenium.webdriver.common.keys import Keys
    from bs4 import BeautifulSoup
    import csv

    element = driver.find_elements(by=By.CSS_SELECTOR,value='p.item_name')

    #n번째 상품 클릭
    link = element[n].find_element(by=By.TAG_NAME,value='a')
    link.send_keys(Keys.ENTER)

    # 최근 열린 탭으로 전환
    driver.switch_to.window(driver.window_handles[-1])

    #URL에 해당하는 페이지의 HTML를 가져옴
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')

    #기본정보 저장
    contents = soup.find_all('dd', class_ = 'text__seller-contents')
    item_title = soup.find('p',class_='text__item-title')

    #text값 가져오기
    product_name = item_title.get_text()
    Seller_name = contents[0].get_text()
    Company = contents[1].get_text()
    BRN = contents[2].get_text()
    contact = contents[3].get_text()
    email = contents[6].get_text()
    product_url = driver.current_url

    #순위
    rank_num = n+1

    #csv 파일에 저장
    row = [today,Market[0],rank_num,product_name,Seller_name,Company,BRN,contact,email,product_url]

    #now we are appending data to the csv
    with open(file_name,'a+',newline='', encoding='cp949') as f:
            writer = csv.writer(f)
            writer.writerow(row)

    #탭 종료
    driver.close()

    #브라우저 전환
    driver.switch_to.window(driver.window_handles[-1])

#데이터 생성
for i in range(end_rank):  #순위 확인
    row_maker(i)

#브라우저 전환
driver.switch_to.window(driver.window_handles[-1])


#######이제부터 MY 스크래핑을 시작하지
#말레이 사이트 전환
go_over = driver.find_element(by=By.XPATH,value='//*[@id="nation10"]/a')
go_over.send_keys(Keys.ENTER)

#오늘의 랭크 확인
rank_today = driver.find_elements(by=By.CSS_SELECTOR,value='span.rank')
end_rank = rank_today[-1].text
end_rank = int(end_rank)
print("오늘의 순위",end_rank,"위 까지")

def row_maker(n):
    from selenium.webdriver.common.keys import Keys
    from bs4 import BeautifulSoup
    import csv

    element = driver.find_elements(by=By.CSS_SELECTOR,value='p.item_name')

    #n번째 상품 클릭
    link = element[n].find_element(by=By.TAG_NAME,value='a')
    link.send_keys(Keys.ENTER)

    # 최근 열린 탭으로 전환
    driver.switch_to.window(driver.window_handles[-1])

    #URL에 해당하는 페이지의 HTML를 가져옴
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')

    #기본정보 저장
    contents = soup.find_all('dd', class_ = 'text__seller-contents')
    item_title = soup.find('p',class_='text__item-title')

    #text값 가져오기
    product_name = item_title.get_text()
    Seller_name = contents[0].get_text()
    Company = contents[1].get_text()
    BRN = contents[2].get_text()
    contact = contents[3].get_text()
    email = contents[6].get_text()
    product_url = driver.current_url

    #순위
    rank_num = n+1

    #csv 파일에 저장
    row = [today,Market[1],rank_num,product_name,Seller_name,Company,BRN,contact,email,product_url]

    #now we are appending data to the csv
    with open(file_name,'a+',newline='', encoding='cp949') as f:
            writer = csv.writer(f)
            writer.writerow(row)

        #탭 종료
    driver.close()

    #브라우저 전환
    driver.switch_to.window(driver.window_handles[-1])

#데이터 생성
for i in range(end_rank):  #순위 확인
    row_maker(i)

#브라우저 전환
driver.switch_to.window(driver.window_handles[-1])


#######이제부터 TW 스크래핑을 시작하지
#TW 사이트 전환
go_over = driver.find_element(by=By.XPATH,value='//*[@id="nation2"]/a')
go_over.send_keys(Keys.ENTER)

#오늘의 랭크 확인
rank_today = driver.find_elements(by=By.CSS_SELECTOR,value='span.rank')
end_rank = rank_today[-1].text
end_rank = int(end_rank)
print("오늘의 순위",end_rank,"위 까지")

def row_maker(n):
    from selenium.webdriver.common.keys import Keys
    from bs4 import BeautifulSoup
    import csv

    element = driver.find_elements(by=By.CSS_SELECTOR,value='p.item_name')

    #n번째 상품 클릭
    link = element[n].find_element(by=By.TAG_NAME,value='a')
    link.send_keys(Keys.ENTER)

    # 최근 열린 탭으로 전환
    driver.switch_to.window(driver.window_handles[-1])

    #URL에 해당하는 페이지의 HTML를 가져옴
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')

    #기본정보 저장
    contents = soup.find_all('dd', class_ = 'text__seller-contents')
    item_title = soup.find('p',class_='text__item-title')

    #text값 가져오기
    product_name = item_title.get_text()
    Seller_name = contents[0].get_text()
    Company = contents[1].get_text()
    BRN = contents[2].get_text()
    contact = contents[3].get_text()
    email = contents[6].get_text()
    product_url = driver.current_url

    #순위
    rank_num = n+1

    #csv 파일에 저장
    row = [today,Market[2],rank_num,product_name,Seller_name,Company,BRN,contact,email,product_url]

    #now we are appending data to the csv
    with open(file_name,'a+',newline='', encoding='cp949') as f:
            writer = csv.writer(f)
            writer.writerow(row)

    #탭 종료
    driver.close()

    #브라우저 전환
    driver.switch_to.window(driver.window_handles[-1])

#데이터 생성
for i in range(end_rank):  #순위 확인
    row_maker(i)

#브라우저 종료
driver.switch_to.window(driver.window_handles[-1])
driver.quit()