#!/usr/bin/env python
# coding: utf-8
#완성 코드

num_list =[]

for i in range(0,200,10):
    num = i
    num_list.append(num)

title = []
link = []

for number in num_list:
    URL = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={search_word}&sort=0&photo=0&field=0&pd=3&ds={startdate}&de={enddate}&cluster_rank=37&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from{start_date}to{end_date},a:all&start={page_num}'
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
    url = URL.format(search_word = '서초맛집',startdate= '2021.08.01',enddate = '2021.08.05',
                                   start_date='20210801',end_date = '20210801',page_num = number)
    
    response = requests.get(url, headers = headers)
    soup=BeautifulSoup(response.text,'lxml')
    articles = soup.find_all('div', {'class' : 'news_area'})    
    
    
    for article in articles:
        article_title = article.find('a', attrs = {'class' : 'news_tit'})['title']
        print('제목: ', article_title)
        article_link = article.find('a', attrs = {'class' : 'news_tit'})['href']
        print('링크 : ', article_link)
        print('\n')
        title.append(article_title)
        link.append(article_link)

import pandas as pd
df = pd.DataFrame({'제목': title,
                   '링크' : link})
df.to_excel('corona.xlsx')