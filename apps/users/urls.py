# -*- coding:utf-8 -*-
__author__ = 'gjw'
__date__ = '2017/1/24 9:47'

from django.conf.urls import url, include

from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView
from .views import MyCourseView, MyFavOrgView, MyFavTeacherView, MyFavCoureseView, MyMessageView

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),

    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),

    # 用户密码修改
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name='update_pwd'),

    # 发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name='sendemail_code'),

    # 修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name='update_email'),

    # 我的课程
    url(r'^mycourse/$', MyCourseView.as_view(), name='mycourse'),

    # 我收藏的课程机构
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name='myfav_org'),

    # 我收藏的授课讲师
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name='myfav_teacher'),

    # 我收藏的课程
    url(r'^myfav/course/$', MyFavCoureseView.as_view(), name='myfav_course'),

    # 我的消息
    url(r'^mymessage/$', MyMessageView.as_view(), name='mymessage'),

]