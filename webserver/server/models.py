from contextlib import AbstractAsyncContextManager
from email.policy import default
from logging import StringTemplateStyle
from pickletools import stringnl
from pydoc import doc
import re
from sqlite3 import Date
from unicodedata import category, name
from unittest.util import _MAX_LENGTH
from django.db import models
from mongoengine import *
from pkg_resources import require
# Create your models here.
# EmbeddedDocument

class Periodicals(Document):                               ##期刊信息
    PeriodicalName = StringField(max_length=50)                     ##期刊名
    VolumeNumber = StringField(max_length=10)                       ##期刊卷号
    IssueNumber = StringField(max_length=10)                        ##期刊期号
    Institution = StringField(max_length=100)                       ##创办机构
    Category = StringField(max_length=20)                           ##期刊类别
    PeriodicalUrl = StringField(max_length=100) 

class Periodical(EmbeddedDocument):                               ##期刊信息
    PeriodicalName = StringField(max_length=50)                     ##期刊名
    VolumeNumber = StringField(max_length=10)                       ##期刊卷号
    IssueNumber = StringField(max_length=10)                        ##期刊期号
    Institution = StringField(max_length=100)                       ##创办机构
    Category = StringField(max_length=20)                           ##期刊类别
    PeriodicalUrl = StringField(max_length=100)                     ##期刊连接

class Meeting(EmbeddedDocument):                                  ##会议信息
    MeetName = StringField(max_length=50)                           ##会议名
    Meetdate = StringField(max_length=10)                           ##会议时间
    MeetPlace = StringField(max_length=100)                         ##会议地点
    Institution = StringField(max_length=100)                       ##主办单位
    MeetTerm = IntField()                                           ##会议届数
    MeetUrl = StringField(max_length=100)                           ##会议超链接

class Meetings(Document):                                  ##会议信息
    MeetName = StringField(max_length=50)                           ##会议名
    Meetdate = StringField(max_length=10)                           ##会议时间
    MeetPlace = StringField(max_length=100)                         ##会议地点
    Institution = StringField(max_length=100)                       ##主办单位
    MeetTerm = IntField()                                           ##会议届数
    MeetUrl = StringField(max_length=100) 

class Papers(Document):                                    ##论文信息
    PaperId = IntField()                                            ##论文编号
    Tag = IntField()                                                ##论文来源标识，若为1则来源期刊，为2则来源会议
    PaperName  = StringField(max_length=100,require = True)         ##论文标题
    KeyWords = ListField(max_length=10)                             ##关键字
    Abstract = StringField(max_length=400)                          ##摘要
    Authors = ListField(max_length=10)                              ##作者信息
    periodical = EmbeddedDocumentField(Periodical)                  ##来源期刊信息
    meeting = EmbeddedDocumentField(Meeting)                        ##来源会议信息
    PublicTime = StringField(max_length=10)                         ##发布时间
    PaperUrl = StringField(max_length=100)                          ##论文连接


class Paper(EmbeddedDocument):                                    ##论文信息
    PaperId = IntField()                                            ##论文编号
    Tag = IntField()                                                ##论文来源标识，若为1则来源期刊，为2则来源会议
    PaperName  = StringField(max_length=100,require = True)         ##论文标题
    KeyWords = ListField(max_length=10)                             ##关键字
    Abstract = StringField(max_length=400)                          ##摘要
    Authors = ListField(max_length=10)                              ##作者信息
    periodical = EmbeddedDocumentField(Periodical)                  ##来源期刊信息
    meeting = EmbeddedDocumentField(Meeting)                        ##来源会议信息
    PublicTime = StringField(max_length=10)                         ##发布时间
    PaperUrl = StringField(max_length=100)                          ##论文连接

class Projects(Document):                                  ##项目信息
    ProjectId = IntField()                                          ##项目编号
    ProjectName = StringField(max_length=50)                        ##项目名称
    Introduction = StringField(max_length=300)                      ##项目介绍                   
    Participants = ListField(max_length=20)                         ##参与人员
    Process  = StringField(max_length=50)                           ##项目进展
    DateInOut = StringField(max_length=30)                          ##起始时间
    Direction = StringField(max_length=30)                          ##研究方向
    Achievement = StringField(max_length=100)

class Project(EmbeddedDocument):                                  ##项目信息
    ProjectId = IntField()                                          ##项目编号
    ProjectName = StringField(max_length=50)                        ##项目名称
    Introduction = StringField(max_length=300)                      ##项目介绍                   
    Participants = ListField(max_length=20)                         ##参与人员
    Process  = StringField(max_length=50)                           ##项目进展
    DateInOut = StringField(max_length=30)                          ##起始时间
    Direction = StringField(max_length=30)                          ##研究方向
    Achievement = StringField(max_length=100)                       ##研究成果

class   Peopleinfo(Document):                                ##个人信息
    Name =  StringField(max_length=10)                                  
    Avtar = StringField(max_length=150)                             ##头像信息
    Mail = StringField(max_length=50)                               ##个人邮箱
    Direction = StringField(max_length=50)                          ##研究方向
    Awards = StringField(max_length=150)                            ##获奖情况
    paperlist = ListField(EmbeddedDocumentField(Paper),max_length=10)       ##名下论文
    projects = ListField(EmbeddedDocumentField(Project),max_length=10)


class GroupMeeting(EmbeddedDocument):                             ##组会信息
    MeetingPhotoUrl = StringField(max_length=100)                   ##图片路由
    Speaker = StringField(max_length=10)                            ##主讲人
    Content = StringField(max_length=150)                           ##主讲内容
    Time = StringField(max_length=20)                               ##组会时间

class DailyActivity(EmbeddedDocument):                            ##活日常动信息
    ActivityPhotoUrl = StringField(max_length=100)                  ##活动图片路由
    Title = StringField(max_length=150)                             ##活动标题
    Time = StringField(max_length=20)                               ##活动时间


class Activities(Document):                              ##所有活动信息
    Tag = IntField()
    GroupMeeting = EmbeddedDocumentField(GroupMeeting)   ##组会列表
    DailyActivity = EmbeddedDocumentField(DailyActivity) ##日常活动列表