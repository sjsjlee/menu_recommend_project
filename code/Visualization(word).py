
import pandas as pd

text_file = open("C:\\Users\\samsung\\Desktop\\lunch_menu_s.txt", 'r')

lunch_text = text_file.read()

print(lunch_text)



from konlpy.tag import Okt

okt = Okt()
nouns = okt.nouns



menu_nouns = okt.nouns(lunch_text)



from collections import Counter
count = Counter(menu_nouns)

tag_count = []
tags = []

for n, c in count.most_common(100):
    dics = {'tag': n, "count" : c}
    if len(dics['tag'])>=2 and len(tags) <= 49 :
        tag_count.append(dics)
        tags.append(dics['tag'])




for tag in tag_count :
    print("{:<14}".format(tag['tag']), end='\t')
    print("{}".format(tag['count']))



count.most_common(100)




word_counter =count.most_common(30)


word_data = pd.DataFrame(word_counter,
                        columns = ['menu', 'count'])

word_data




import matplotlib.pyplot as plt


word_data.plot(kind= 'barh', title = 'menu count')

plt.rc('font', size =5)
plt.show()


import seaborn as sns



import matplotlib.font_manager as fm

font_list = fm.findSystemFonts(fontpaths = None, fontext = 'ttf')

font_list[:]


path = 'C:\\Users\\samsung\\Downloads\\NanumBarunGothic.ttf'
fontprop = fm.FontProperties(fname=path, size = 18)


fig, ax = plt.subplots(figsize = (10,10))

word_data.sort_values(by = 'count').plot.barh(x='menu', y='count',
                                             ax = ax,
                                             color = 'salmon')

ax.set_title("lunch menu count")

plt.rcParams["font.family"] = 'NanumGothic'
plt.rc('font', size = 15)





