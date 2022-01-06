from gtts import gTTS

mytx='Dhananjay having lunch at this time'
language='en'
myobj=gTTS(text=mytx,lang=language,tld="ca")
myobj.save('dha.mp3')


import pytube
link="https://youtu.be/hl24ffI-vFg"
yt=pytube.YouTube(link)
stream=yt.streams.first()   
stream.download()