#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
from selenium import webdriver
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

search_keyword = '서초맛집'
URL = 'https://search.naver.com/search.naver?where=blog&query={}&sm=tab_opt&nso=so%3Ar%2Cp%3Afrom{}to{}'
#url = URL.format(quote(search_keyword), date, date)


date_list = []
for date_num in range(20200101, 20200103, 1):
    date_num = date_num
    date_list.append(date_num)
    #print(date_list)

title = []
text = []

for date in date_list:
    URL = 'https://search.naver.com/search.naver?where=blog&query={}&sm=tab_opt&nso=so%3Ar%2Cp%3Afrom{}to{}'
    url = URL.format(quote(search_keyword), date, date)
    #print(url)
    
    driver = webdriver.Chrome("C:\\Users\\samsung\\Desktop\\jupyter\\chromedriver_win32\\chromedriver.exe")
    driver.get(url)
    scroll_pause_time = 2

    last_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    while True:
        try :
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            #페이지 로드 기다림
            time.sleep(scroll_pause_time)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
            time.sleep(scroll_pause_time)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight") 


            # 새로운 높이가 이전 높이와 변하지 않았을 경우 스크롤 종료
            if new_height == last_height:
                break


            # 스크롤 다운이 된다면 스크롤 다운이 된 후의 창 높이를 새로운 높이로 갱신
            last_height = new_height

            #크롤링
            soup = BeautifulSoup(driver.page_source, 'lxml')
            posts = soup.find_all('div', attrs={'class':'total_area'})

        except :
            print('error')
            break
            
    #크롤링
    soup = BeautifulSoup(driver.page_source, 'lxml')
    posts = soup.find_all('div', attrs={'class':'total_area'})

    # 본문 복사 금지(iframe) 제거 후 크롤링 작업 준비

    def delete_iframe(url) :

      headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
      res = requests.get(url, headers = headers)
      #res.raise_for_status()
      soup = BeautifulSoup(res.text, 'lxml')

      src_url = "https://blog.naver.com/" + soup.iframe['src']

      return src_url

    def text_scraping(url):
      headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
      res = requests.get(url, headers = headers)
      #res.raise_for_status()
      soup = BeautifulSoup(res.text, 'lxml')

      if soup.find('div', attrs = {'class': 'se-main-container'}):
        text = soup.find('div', attrs ={'class':'se-main-container'}).get_text()
        text = text.replace('\n', '')
        return text

      elif soup.find('div', attrs = {'id': "postViewArea"}): #스마트에디터
        text = soup.find('div', attrs = {'id': "postViewArea"}).get_text()
        text = text.replace('\n', '')
        return text

      elif soup.find('div', attrs = {'class' : "__se_component_area"}): #2018년 이전 html 코드 대상
        text = soup.find('div', attrs = {'class' : "__se_component_area"}).get_text()
        text = text.replace('\n', '')
        return text

      else:
        return '확인불가'

    #제목, 본문만 크롤링

    for post in posts:
        post_title = post.find('a', attrs = {'class' : 'api_txt_lines total_tit'}).get_text()
        print("제목:", post_title)
        post_link = post.find('a', attrs = {'class' : 'api_txt_lines total_tit'})['href']
        #print('link :', post_link)
        print('-'*50)

        blog_p = re.compile('blog.naver.com') #블로그 주소만 크롤링
        blog_m = blog_p.search(post_link)

        try :
            if blog_m :
                blog_text = text_scraping(delete_iframe(post_link))
                print(blog_text)
                print('-'*50)
                
                title.append(post_title)
                text.append(blog_text)
        except TypeError:
            print('삭제된 페이지')

        #title.append(post_title)
        #link.append(post_link)
        #text.append(blog_text)

    '''dates = [dates.get_text() for dates in soup.find_all('span', attrs={'class':'etc_dsc_area'})]

    dates_list = []
    for date_i in dates:
        if re.search(r'\d+.\d+.\d+', date_i) != None:
            dates_list.append(date_i)'''


# In[ ]:


import pandas as pd

df = pd.DataFrame({
    '제목' : title,
    '본문' : text,
    #'날짜' : dates_list
})


# In[ ]:


df.head()


# In[ ]:


df.to_csv('seocho_review_crawling.csv')

