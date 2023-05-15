from .models import *
def getproject(process):
    lists = []
    print(process)
    res = Projects.objects.filter(Process = process)
    for i in res:
        list = {}
        list['ProjectId'] = i.ProjectId
        list['ProjectName'] = i.ProjectName
        list['Introduction'] = i.Introduction
        list['Participants'] = i.Participants
        list['DateInOut'] = i.DateInOut
        list['Direction'] = i.Direction
        list['Achievement'] = i.Achievement
        lists.append(list)
    return lists

def getyearissue(year):
    lists = []
    print(year)
    for i in Papers.objects:
        print(i.PublicTime)
        if year == i.PublicTime:
            list = {}
            list['PaperId'] = i.PaperId
            list['Tag'] = i.Tag
            list['KeyWords'] = i.KeyWords
            list['Abstract'] = i.Abstract
            list['PaperName'] = i.PaperName
            list['Authors'] = i.Authors
            list['periodical'] = {}
            list['periodical']['PeriodicalName'] = i.periodical.PeriodicalName
            list['periodical']['VolumeNumber'] = i.periodical.VolumeNumber
            list['periodical']['IssueNumber'] = i.periodical.IssueNumber
            list['periodical']['Institution'] = i.periodical.Institution
            list['periodical']['Category'] = i.periodical.Category
            list['periodical']['PeriodicalUrl'] = i.periodical.PeriodicalUrl
            list['meeting'] = {}
            list['meeting']['MeetName'] = i.meeting.MeetName
            list['meeting']['Meetdate'] = i.meeting.Meetdate
            list['meeting']['MeetPlace'] = i.meeting.MeetPlace
            list['meeting']['Institution'] = i.meeting.Institution
            list['meeting']['MeetTerm'] = i.meeting.MeetTerm
            list['meeting']['MeetUrl'] = i.meeting.MeetUrl
            list['PublicTime'] = i.PublicTime
            list['PaperUrl'] = i.PaperUrl
            lists.append(list)
            
    return lists

def getactivity(num):
    lists = []
    numday = 1
    for i in Activities.objects:
        if(numday>(num-1)*6 and numday<=num*6):
            list = {}
            if i.Tag == 1:
                list['Tag'] = i.Tag
                list['MeetingPhotoUrl'] = i.GroupMeeting.MeetingPhotoUrl
                list['Content'] = i.GroupMeeting.Content
                list['Time'] = i.GroupMeeting.Time
                lists.append(list)
            if i.Tag == 0:
                list['Tag'] = i.Tag
                list['ActivityPhotoUrl'] = i.DailyActivity.ActivityPhotoUrl
                list['Title'] = i.DailyActivity.Title
                list['Time'] = i.DailyActivity.Time
                lists.append(list)
        numday = numday + 1
    return lists

def getinfolist(name):
    lists =[]
    list = {}
    print(name)
    i = Peopleinfo.objects.get(Name = name)
    print(i)
    list['Name'] = i.Name
    list['Avtar'] = i.Avtar
    list['Mail'] = i.Mail
    list['Direction'] = i.Direction
    list['Awards'] = i.Awards
    papers = []
    paper = {}
    for j in i.paperlist:
        paper['PaperName'] = j.PaperName
        paper['PublicTime'] = j.PublicTime
        paper['PaperUrl'] = j.PaperUrl
        papers.append(paper)
    list['paperlist'] = papers
    Projects = []
    Pro = {}
    for j in i.projects:
        Pro['ProjectName'] = j.ProjectName
        Pro['Process'] = j.Process
        Projects.append(Pro)
    list['Projects'] = Projects
    lists.append(list)
    return lists
def getmeetinglists():
    lists = []
    for i in Meetings.objects:
        list = {}
        list['MeetName'] = i.MeetName
        list['Meetdate'] = i.Meetdate
        list['MeetPlace'] = i.MeetPlace
        list['Institution'] = i.Institution
        list['MeetTerm'] = i.MeetTerm
        list['MeetUrl'] = i.MeetUrl
        lists.append(list)
    return lists

def getperiodicallists():
    lists = []
    for i in Periodicals.objects:
        list = {}
        list['PeriodicalName'] = i.PeriodicalName
        list['VolumeNumber'] = i.VolumeNumber
        list['IssueNumber'] = i.IssueNumber
        list['Institution'] = i.Institution
        list['Category'] = i.Category
        list['PeriodicalUrl'] = i.PeriodicalUrl
        lists.append(list)
    return lists

def updateinfo():
    groupmeeting = GroupMeeting(MeetingPhotoUrl = '图片URL' , Speaker = '主讲人',
        Content = '主讲内容' ,   Time = '组会时间' 
    )
    dailyactivity = DailyActivity(ActivityPhotoUrl = '图片URL' , 
        Title = '图片标题' , Time = '活动时间'
    )
    activities = Activities(Tag = 1 , GroupMeeting = groupmeeting , DailyActivity = dailyactivity)
    activities.save()
    print(activities)
    projects = Projects(ProjectId = 1,ProjectName = '项目名' , Introduction = '项目介绍' ,
        Participants = ['罗禹中','涂可骋','龙佑熙'], Process = '项目进度' , DateInOut = '起始时间' ,
        Direction = '研究方向' , Achievement = '研究成果'
    )
    projects.save()
    project = Project(ProjectId = 1,ProjectName = '项目名' , Introduction = '项目介绍' ,
        Participants = ['罗禹中','涂可骋','龙佑熙'], Process = '项目进度' , DateInOut = '起始时间' ,
        Direction = '研究方向' , Achievement = '研究成果'
    )
    periodical = Periodical(PeriodicalName = '期刊名称' , VolumeNumber = '期刊卷号',
        IssueNumber = '期刊期号' , Institution = '创办机构' , Category = '期刊类别',
        PeriodicalUrl = '期刊连接'
    )
    meeting = Meeting(MeetName = '会议名称' , Meetdate = '会议时间',
        MeetPlace = '会议地点' , Institution = '创办机构' , MeetTerm = 1 ,
        MeetUrl = '会议连接'
    )
    paper = Paper(PaperId = 1 , Tag = 1,PaperName = '论文名称',
        KeyWords = ['关键字','关键词'] , Abstract = '摘要' , Authors = ['涂可骋','龙佑熙','罗禹中'] ,
        periodical = periodical , meeting = meeting , PublicTime = '发布时间' , PaperUrl = '论文链接'
    )
    peopleinfo =  Peopleinfo(Name = '罗禹中', Avtar = '头像路径' , Mail = '个人邮箱' , Direction = '个人研究方向' , 
        Awards = '获奖情况' , paperlist = [paper] , projects = [project] 
    )
    peopleinfo.save()
   
    periodicals = Periodicals(PeriodicalName = '期刊名称' , VolumeNumber = '期刊卷号',
        IssueNumber = '期刊期号' , Institution = '创办机构' , Category = '期刊类别',
        PeriodicalUrl = '期刊连接'
    )
    periodicals.save()
    meetings = Meetings(MeetName = '会议名称' , Meetdate = '会议时间',
        MeetPlace = '会议地点' , Institution = '创办机构' , MeetTerm = 1 ,
        MeetUrl = '会议连接'
    )
    meetings.save()
    periodical = Periodical(PeriodicalName = '期刊名称' , VolumeNumber = '期刊卷号',
        IssueNumber = '期刊期号' , Institution = '创办机构' , Category = '期刊类别',
        PeriodicalUrl = '期刊连接'
    )
    meeting = Meeting(MeetName = '会议名称' , Meetdate = '会议时间',
        MeetPlace = '会议地点' , Institution = '创办机构' , MeetTerm = 1 ,
        MeetUrl = '会议连接'
    )
    papers = Papers(PaperId = 1 , Tag = 1,PaperName = '论文名称',
        KeyWords = ['关键字','关键词'] , Abstract = '摘要' , Authors = ['涂可骋','龙佑熙','罗禹中'] ,
        periodical = periodical , meeting = meeting , PublicTime = '发布时间' , PaperUrl = '论文链接'
    )
    papers.save()
    Projectss = Projects(ProjectId = 1 , ProjectName = '项目名称' , Introduction = '项目简介' ,
        Participants = ['涂可骋','龙佑熙','罗禹中'] , Process = '已完成' , DateInOut = '2022-08-24',
        Direction = '研究方向' , Achievement = '研究成果'
    )
    Projectss.save()
    return 0