# -*- coding:utf-8 -*-

"""Mxonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls import include, url

import xadmin
from django.views.static import serve


from users.views import LoginView, RegisterView, ActiveUserView,ForgetPwdView,ResetView, ModifyPwdView, LogoutView, IndexView
from organization.views import OrgView
from Mxonline.settings import MEDIA_ROOT
from Mxonline.settings import STATIC_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # 首页url配置
    url('^$', IndexView.as_view(), name="index"),
    # 登录url配置
    url('^login/$', LoginView.as_view(), name="login"),
    # 登出url配置
    url('^logout/$', LogoutView.as_view(), name="logout"),
    # 注册url配置
    url('^register/$', RegisterView.as_view(), name="register"),
    # 验证码工具url配置
    url(r'^captcha/', include('captcha.urls')),
    # 邮箱验证码url（提取变量）
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    # 忘记密码
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),

    # 课程机构url配置
    url(r'^org/', include('organization.urls', namespace='org')),

    # 课程相关url配置
    url(r'^course/', include('courses.urls', namespace='course')),

    # 用户相关url配置
    url(r'^users/', include('users.urls', namespace='users')),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 富文本相关url
    url(r'^ueditor/', include('DjangoUeditor.urls' )),

    # 生产环境static url配置
    url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),


]
# 全局404页面配置
handler404 = 'users.views.page_not_found'
# 全局500页面配置
handler500 = 'users.views.page_error'
