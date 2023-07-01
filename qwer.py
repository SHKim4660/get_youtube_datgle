from bs4 import BeautifulSoup
import selenium
import time
from konlpy.tag import Okt
from konlpy.tag import Kkma
from selenium.webdriver.common.keys import Keys
from selenium import webdriver # webdriver를 이용해 해당 브라우저를 열기 위해
from selenium.webdriver.common.by import By # html요소 탐색을 할 수 있게 하기 위해
from selenium.webdriver.support.ui import WebDriverWait # 브라우저의 응답을 기다릴 수 있게 하기 위해
from selenium.webdriver.support import expected_conditions as EC # html요소의 상태를 체크할 수 있게 하기 위해
5
dr = webdriver.Chrome("C:/Users/John/Documents/GitHub/yt_datgle_crw/chromedriver.exe")
dr.get('https://www.youtube.com/watch?v=wipPwMM5Oe0')

time.sleep(10)

dr.execute_script("window.scrollTo(0, 700)")

time.sleep(2)
a = []
for i in range(1,6):
    datgle = dr.find_element(By.XPATH,f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[{i}]/ytd-comment-renderer/div[3]/div[2]/div[2]/ytd-expander/div/yt-formatted-string').text#.replace(".","").replace("?","").split(" ")
    a.append(datgle)
print(a)
# b = []
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         b.append(a[i][j])

# print(b)
kkma = Kkma()

for i in range(len(a)):
    kkma.pos(a[i])


while True:
    pass