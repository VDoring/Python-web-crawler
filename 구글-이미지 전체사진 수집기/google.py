# https://www.youtube.com/watch?v=1b7pXC1-IbE&t=286s

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

# Chrome 시크릿모드를 위한 필수 코드
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")

elem = driver.find_element_by_name("q") # 요소 찾기 (이 코드는 구글 검색참을 찾는다)
elem.send_keys('eraser') # 원하는 입력 값
elem.send_keys(Keys.RETURN) # Enter키 입력

SCROLL_PAUSE_TIME = 1.1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight") # JavaScript코드 실행. 브라우저의 높이를 알 수 있다

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") # "rg_i Q4LuWd" 라는 class를 가진 요소
count = 1
for image in images: # 모든 (작은)이미지들 중에서 하나씩 가져오는 반복문.
    try:
        image.click()
        time.sleep(2.2) # 지연시간
        imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img').get_attribute("src") # n3VNCb라는 class를 가진 요소 하나를 선택하고, src 값을 가져온다.
        urllib.request.urlretrieve(imgUrl, str(count)+".jpg") # 이미지의 주소, 이미지 저장할 이름
        count += 1
        print('Downloaded:',imgUrl)
    except:
        pass

driver.close()