from django.urls import path
from server import views

urlpatterns = [
    path("index/", views.index),
    path('issuelist/',views.getissuelist),
    path('projectlist/',views.getprojectlist),
    path('activelist/',views.getactivelist),
    path('userinfo/',views.getuserinfo),
    path('update/',views.update),
    path('meetinglist',views.getmeetinglist),
    path('periodicallist',views.getperiodicallist)
]