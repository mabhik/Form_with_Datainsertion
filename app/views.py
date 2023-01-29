from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        t=topic.objects.get_or_create(topic_name=tn)[0]
        t.save()
        return HttpResponse('insertion of topic is done')
    return render(request, 'insert_topic.html')

def insert_webpage(request):
    if request.method=='POST':
        tn=request.POST['webpage']
        t=topic.objects.get_or_create(topic_name=tn)[0]
        t.save()
        n=request.POST['nme']
        nm=topic.objects.get_or_create(topic_name=n)[0]
        nm.save()
        u=request.POST['url']
        ur=topic.objects.get_or_create(topic_name=u)[0]
        ur.save()
        return HttpResponse('insertion of topic is done')
    return render(request, 'insert_topic.html')