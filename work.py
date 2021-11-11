# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 13:14:43 2021

@author: yoshimura yuta
"""

mylib=["52ヘルツのクジラたち","具体と抽象",'ドキュメント']
import pandas as pd

df=pd.read_csv('book_date.csv',encoding='UTF-8')
def my_list() :
    print('----------------------------------------')
    print('持っている本リスト')
    print(mylib)

x=df["タイトル"]

    
 
print(x)