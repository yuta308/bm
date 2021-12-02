# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 13:41:39 2021

@author: yoshimura yuta
"""
import streamlit as st
import requests
import json
import requests
import io
import time
from PIL import Image



def google():
    if len(tool)>=1 and len(want)>=1:
         
        url = 'https://www.googleapis.com/books/v1/volumes?q='+str(tool)+str(want)  #GooglBooksAPI
        response = requests.get(url).json() #情報の取得,json変換
        totalitems = response['totalItems'] #件数1
        st.write('検索結果は',str(totalitems),'件です')
        for i in range(0,int(a)) :
            col1,col2 = st.columns(2)
            try :
                 items_list = response['items'] #items リストデータ
                 items = items_list[i] #items
                 info = items['volumeInfo']
                 title = info['title']
                 pagelink = info['canonicalVolumeLink']
                 description = info['description']
                 pagecount=info['pageCount']
                 authors=info['authors'][0]
                 publishdate=info['publishedDate']
                 pic=info['imageLinks']['thumbnail']
                 with col2 :
                     st.write('タイトル：', title)
                     st.write('著者：',authors)
                     st.write('発売日：',publishdate)
                     st.write('ページ数:',str(pagecount)+'ページ')
                     st.write('URL',pagelink)
                     st.write('紹介文')
                     st.write(description)
                     st.write('')
                     st.write('')
                 with col1 :
                     a_img = Image.open(io.BytesIO(requests.get(pic).content))
                     st.image(a_img, width=190)
                     time.sleep(0.5)
            except KeyError:
                st.write('検索結果がみつかりませんでした')
                st.write('もう一度試してください')
                st.stop()
        
    else :
        pass
 
col1, col2, =st.columns(2)
with col1 :
    ime=Image.open('name.png')
    st.image(ime)
with col2 :
    img=Image.open('book.png')
    st.image(img,width=150)
    

st.header('調べる方法を選んでください')
st.write('１：タイトル　２：著者　３　ISBN_4　フリーワード')
tool = st.selectbox('好きな数字を教えてください',list(['1','2','3','4']))
a = int(st.slider('何件表示させますか？',0,10,5))


if tool == '1' :
    tool='intittle:'
    want=st.text_input('調べたい本のタイトルを入力してください')
    google()
elif tool == '2' :
    tool='inauthor:'
    want=st.text_input('調べたい本の著者を入力してください')
    google()
elif tool == '3' :
    tool = 'isbn:'
    want=st.text_input('調べたい本のISBN（１０桁または１３桁）の数字を入力してください')
    google()
elif tool == '4' :
    want = st.text_input('フリーワードで調べることが出来ます')
    google()
else :
    st.write('最初からやり直してください')
