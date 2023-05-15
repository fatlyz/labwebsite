import imp
from sre_constants import SUCCESS
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from server.opreate import * 
from ast import dump
import json
from django.http import HttpResponseRedirect
# Create your views here.
def update(request):
    updateinfo()
    return HttpResponse(1)

def index(request):
    return HttpResponseRedirect("/static/首页.html")

def getissuelist(request):
    if request.method == 'POST':
        year = request.POST.get('year')
    if request.method == 'GET':
        year = request.GET.get('year')
    issuelist = getyearissue(year)
    issuelist = json.dumps(issuelist,ensure_ascii=False)
    return HttpResponse(issuelist)

def getprojectlist(request):
    if request.method == 'POST':
        process = request.POST.get('process')
    if request.method == 'GET':
        process = request.GET.get('process')
    project = getproject(process)
    project = json.dumps(project,ensure_ascii=False)
    return HttpResponse(project)

def getactivelist(request):
    ##活动列表查询
    if request.method == 'POST':
        num = request.POST.get('number')
    if request.method == 'GET':
        num = request.GET.get('number')
    num = int(num)
    activitylist = getactivity(num)
    activitylist =json.dumps(activitylist,ensure_ascii=False)
    return HttpResponse(activitylist)

def getuserinfo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
    if request.method == 'GET':
        name = request.GET.get('name')
    infolist = getinfolist(name)
    infolist = json.dumps(infolist,ensure_ascii=False)
    return HttpResponse(infolist)

def getmeetinglist(request):
    meetinglist = getmeetinglists()
    meetinglist = json.dumps(meetinglist,ensure_ascii=False)
    return HttpResponse(meetinglist)

def getperiodicallist(request):
    periodicallist = getperiodicallists()
    periodicallist = json.dumps(periodicallist,ensure_ascii=False)
    return HttpResponse(periodicallist)

# def getissuelist(request):
    
#     return HttpResponse('你获取到了论文列表了')

# def getissuelist(request):
    
#     return HttpResponse('你获取到了论文列表了')