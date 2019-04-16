# -*- coding: utf-8 -*-
__author__ = 'heroli'
#wordcloud生成中文词云
from wordcloud import WordCloud
import jieba
# 词频计算
import jieba.analyse as analyse
from scipy.misc import imread
import os
from os import path
import matplotlib.pyplot as plt
 
class WC(object):
 
    # 绘制词云
    def draw_wordcloud(self):
        #读入一个txt文件
        comment_text = open('static/test.txt','r').read()
        #结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云
        cut_text = " ".join(jieba.cut(comment_text))
        result = jieba.analyse.textrank(cut_text, topK=1000, withWeight=True)
        # 生成关键词比重字典
        keywords = dict()
 
        for i in result:
            keywords[i[0]] = i[1]
 
        d = path.dirname(__file__) # 当前文件文件夹所在目录
        color_mask = imread("static/images/alice.png") # 读取背景图片
        cloud = WordCloud(
            #设置字体，不指定就会出现乱码
            font_path="./fonts/Simfang.ttf",
            # font_path=path.join(d,'simsun.ttc'),
            width=200,
            height=200,
            #设置背景色
            background_color='white',
            #词云形状
            mask=color_mask,
            #允许最大词汇
            max_words=2000,
            #最大号字体
            max_font_size=40
        )
        word_cloud = cloud.generate(cut_text)# 产生词云
        word_cloud.to_file("static/images/user_img.jpg") #保存图片
        #  显示词云图片
        # plt.imshow(word_cloud)
        # plt.axis('off')
        # plt.show()
 
 
if __name__ == '__main__':
    wc = WC()
    wc.draw_wordcloud()