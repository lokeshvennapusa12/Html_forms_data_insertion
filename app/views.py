from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic inserted Successfully')
        

    return render(request,'insert_topic.html')

def insert_webpage(request):
    topics=Topic.objects.all()
    d={'topics':topics}


    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
        WO.save()

        return HttpResponse('Webpage inserted Successfully')
    return render(request,'insert_webpage.html',context=d)


def insert_access(request):
    webpage=Webpage.objects.all()
    d={'webpage':webpage}


    if request.method=='POST':
        na=request.POST['na']
        au=request.POST['au']
        da=request.POST['da']
        # TO=Topic.objects.get_or_create(topic_name=tn)[0]
        # TO.save()
        WO=Webpage.objects.get_or_create(name=na)[0]
        WO.save()
        AO=AccessRecords.objects.get_or_create(name=WO,author=au,date=da)[0]
        AO.save()

        return HttpResponse('Access Records inserted Successfully')
    return render(request,'insert_access.html',context=d)



