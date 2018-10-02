# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 11:02:45 2018

"""

from bs4 import BeautifulSoup
import re
import time
import requests
import pandas
list1=[]
def run(fname):

   

   

		
    html=open(fname,'r')
      
    soup = BeautifulSoup(html,'lxml') # parse the html 

    information=soup.find('ul', {'class':re.compile('content-meta info')})
    try:
        info=information.findAll('li',{'class':'meta-row clearfix'})
    except:
        pass
    #info1=soup.findAll('div',{'class':'superPageFontColor'})
    #count=0
    
    d={}
    
    #***********Movie Name**************************************************
    MovieName1='NA'
    
    try:
        NameChunk=soup.find('h1', {'data-type':re.compile('title')})
        if (NameChunk): MovieName1=NameChunk.text.strip()
        d["Movie Name:"]=str(MovieName1)
    except:
        d["Movie Name:"]="NA"
        
    #************For Audience and Crtis Rating**********************
    ratings=soup.find('div',{'id':re.compile('scorePanel')})
    rating1='NA' # initialize rating
    rating2='NA' # initialize rating
    try:
        RChunk=ratings.find('span', {'class':re.compile('meter-value')})
        if (RChunk): rating1=RChunk.text#.encode('ascii','ignore')
        RChunk2=ratings.find('div', {'class':re.compile('meter-value')})
        if (RChunk2): rating2=RChunk2.text#.encode('ascii','ignore')
        #fl.write(str('critics:'+rating1+'\t'+'audience:'+rating2.strip()+'\t'))
        d["Critics Rating"]=str(rating1)
        d["Audience Rating"]=str(rating2.strip())
    except:
          d["Critics Rating"]="NA"
          d["Audience Rating"]="NA"
    #***********For Cast***************************************
    characters=soup.findAll('div',{'class':re.compile('cast-item media inlineBlock')})
    Cast=""
    try:
        for character in characters:
            castName='NA'
            CChunk=character.find('a',{'class':re.compile('unstyled articleLink')})
            if(CChunk):castName=CChunk.text.strip()
            #fl.write(str(castName+'\t'))
            Cast=castName+", "+Cast
            d["Cast"]=str(Cast)
    except:
            d["Cast"]="NA"
   #*************For Release Date**********************************
    ReleaseDate='NA'
    try:
        ReleaseDate1=information.find('li', {'class':re.compile('meta-row clearfix js-theater-release-dates')})
        ReleaseDate2=ReleaseDate1.find('div', {'class':re.compile('meta-value')})
        if (ReleaseDate2): ReleaseDate=ReleaseDate2.text.strip()
        d["Release Date:"]=str(ReleaseDate)
    except:
        d["Release Date:"]="NA"
    #**********For Rating, genre, director, writtenBy, Runtime, Studio
    #l=["Rating","Genre","Director","Written by","On Disc","Box OFfice","Runtime","Studio"]
    #****************For Fresh Critics Reviews***********************
    '''
    FreshRating='NA'
    FR=info1.find('span', {'class':re.compile('subtle superPageFontColor audience-info')})
    FR1=FR.find('span', {'':re.compile('')})
    if (FR1): FreshRating=FR1.text.strip()
    d["Fresh Reviewa:"]=str()
    '''
    try:
        for inf in info:
        
        
        #print(inf.findAll(attrs={"meta-label subtle" : "Rating:"}))
        #if "Directed By:" in inf.find('div',{'class':'meta-label subtle'}).text: 
        
        #index=l[count]
        #print(index)
            try:
                value=inf.find('div',{'class':'meta-value'}).text.strip() #.encode('ascii','ignore')
                label=inf.find('div',{'class':'meta-label subtle'}).text.strip() #.encode('ascii','ignore')
        #print(label)
                d[label]=value
            except:
                d[label]="NA"
        #count=count+1
        #print(count)
            print(d)
    except:
        pass
        
    #print(d)
    list1.append(d)
    #.append(d)
    df=pandas.DataFrame(list1)
    #print(df)
    df.to_csv("OutputURL2.csv")
        

        
		      
    #l.append(d)
        
    #df=pandas.DataFrame(l)
    #print(df)

if __name__=='__main__':
    url='https://www.rottentomatoes.com/m/a_quiet_place_2018'
    
    f = open('URL1.txt','r')
    
    #considering each url in a new line...
    
    while True:
     URL = f.readline()
     MovieFileName=str(URL.split('https://www.rottentomatoes.com/m/')[1])
     MovieFileName=MovieFileName[:-1]
     print(MovieFileName)
     filename=MovieFileName+'.html'
     run(filename)

