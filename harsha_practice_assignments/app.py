from flask import Flask, render_template
from newsapi import NewsApiClient

app=Flask(__name__)

@app.route('/')
def index():
    newsapi=NewsApiClient(api_key="abaa63e891034611874f0507333e9dac")
    topheadlines=newsapi.get_top_headlines(sources="bbc-news")
    articles =topheadlines['articles']

    desc=[]
    news=[]
    img=[]
    cont=[]
    pub=[]
    url_1=[]

    for i in range((len(articles))):
        myarticles=articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        cont.append(myarticles['content'])
        pub.append(myarticles['publishedAt'])
        url_1.append(myarticles['url'])

    mylist=zip(news,desc,img,cont,pub,url_1)

    return render_template('index.html',context=mylist)


if __name__=='__main__':
    app.run(debug=True)