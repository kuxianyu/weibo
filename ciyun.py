from wordcloud import WordCloud
import PIL
import numpy as np

#读取文本文件
with open('resou.txt','r',encoding='utf-8') as f:
    mytext = f.read()


#生成词云
#指定背景
my_mask = np.array(PIL.Image.open('心形.png'))

#设定参数
mycloud = WordCloud(font_path='msyh.ttc',background_color='white',mask=my_mask).generate(mytext)

#保存到图片
mycloud.to_file('热搜.png')
