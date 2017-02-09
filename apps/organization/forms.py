# -*- coding:utf-8 -*-
__author__ = 'gjw'
__date__ = '2017/1/20 15:47'

import re
from django import forms

from operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    class Meta:
        # 指明所用的model
        model = UserAsk
        # 所需要的字段
        fields = ['name', 'mobile', 'course_name']

# 验证手机号码是否合法
    # form表单验证，函数必须以clean_字段 来命名
    def clean_mobile(self):
        # 取出当前实例的数据
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            # 抛出自定义异常
            raise forms.ValidationError(u"手机号码非法", code='mobile_invalid')
