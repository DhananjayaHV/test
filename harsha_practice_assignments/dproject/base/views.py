from django.shortcuts import render

from django.http import HttpResponse


rooms=[{'id':1, 'name':'Lear python'},
        {'id':2, 'name':'Lear Django'},
        {'id':3, 'name':'Lear Flask'},
        {'id':4, 'name':'Lear FastAPI'}
]

def home(request):
    content={'rooms':rooms}
    return render(request,'base/home.html',content)

def room(request,pk):
    room=None
    for i in rooms:
        if i['id']==int(pk):
            room=i
    content={'room':room}   

    return render(request,'base/room.html',content)