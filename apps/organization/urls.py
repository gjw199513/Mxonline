# -*- coding:utf-8 -*-
__author__ = 'gjw'
__date__ = '2017/1/20 15:57'

from django.conf.urls import url, include

from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView
from .views import TeacherListView, TeacherDetailView
urlpatterns = [
    # 课程机构列表页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    # 我要学习咨询
    url(r'add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    # 机构首页
    url(r'home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
    # 机构课程列表页
    url(r'course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='org_course'),
    # 机构介绍列表页
    url(r'desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name='org_desc'),
    # 机构讲师
    url(r'org_teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='org_teacher'),

    # 机构收藏
    url(r'add_fav/$', AddFavView.as_view(), name='add_fav'),

    # 教师收藏
    url(r'teacher/list/$', TeacherListView.as_view(), name='teacher_list'),

    #讲师详情页
    url(r'teacher/detail/(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name='teacher_detail'),

]
