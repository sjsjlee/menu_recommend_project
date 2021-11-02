#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd

text_file = open("C:\\Users\\samsung\\Desktop\\lunch_menu_s.txt", 'r')

lunch_text = text_file.read()

print(lunch_text)


# In[ ]:





# In[27]:


from konlpy.tag import Okt

okt = Okt()
nouns = okt.nouns


# In[28]:


menu_nouns = okt.nouns(lunch_text)


# In[29]:


from collections import Counter
count = Counter(menu_nouns)

tag_count = []
tags = []

for n, c in count.most_common(100):
    dics = {'tag': n, "count" : c}
    if len(dics['tag'])>=2 and len(tags) <= 49 :
        tag_count.append(dics)
        tags.append(dics['tag'])


# In[30]:



for tag in tag_count :
    print("{:<14}".format(tag['tag']), end='\t')
    print("{}".format(tag['count']))


# In[65]:


count.most_common(100)


# In[106]:


word_counter =count.most_common(30)


# In[111]:


word_data = pd.DataFrame(word_counter,
                        columns = ['menu', 'count'])

word_data


# In[96]:


import matplotlib.pyplot as plt


word_data.plot(kind= 'barh', title = 'menu count')

plt.rc('font', size =5)
plt.show()


# In[66]:


import seaborn as sns


# In[83]:


import matplotlib.font_manager as fm

font_list = fm.findSystemFonts(fontpaths = None, fontext = 'ttf')

font_list[:]


# In[108]:


path = 'C:\\Users\\samsung\\Downloads\\NanumBarunGothic.ttf'
fontprop = fm.FontProperties(fname=path, size = 18)


# In[110]:


fig, ax = plt.subplots(figsize = (10,10))

word_data.sort_values(by = 'count').plot.barh(x='menu', y='count',
                                             ax = ax,
                                             color = 'salmon')

ax.set_title("lunch menu count")

plt.rcParams["font.family"] = 'NanumGothic'
plt.rc('font', size = 15)


# In[ ]:




