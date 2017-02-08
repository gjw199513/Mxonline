# -*- coding:utf-8 -*-
__author__ = 'gjw'
__date__ = '2017/1/14 18:45'

import xadmin

from datetime import datetime
from .models import EmailVerifyRecord, Banner, UserProfile
from xadmin import views
from xadmin.plugins.auth import UserAdmin

#
# class UserProfileAdmin(UserAdmin):
#     # def get_form_layout(self):
#     #     if self.org_obj:
#     #         self.form_layout = (
#     #             Main(
#     #                 Fieldset('',
#     #                          'username', 'password',
#     #                          css_class='unsort no_title'
#     #                          ),
#     #                 Fieldset(_('Personal info'),
#     #                          Row('first_name', 'last_name'),
#     #                          'email'
#     #                          ),
#     #                 Fieldset(_('Permissions'),
#     #                          'groups', 'user_permissions'
#     #                          ),
#     #                 Fieldset(_('Important dates'),
#     #                          'last_login', 'date_joined'
#     #                          ),
#     #             ),
#     #             Side(
#     #                 Fieldset(_('Status'),
#     #                          'is_active', 'is_staff', 'is_superuser',
#     #                          ),
#     #             )
#     #         )
#     #     return super(UserAdmin, self).get_form_layout()
#     pass


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = u"慕学后台管理系统"
    site_footer = u"慕学在线网"
    menu_style = "accordion"


# 邮箱验证码注册
class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    model_icon = 'fa fa-address-book'


# 轮播图注册
class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

# from django.contrib.auth.models import User
# xadmin.site.unregister(User)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
# xadmin.site.register(UserProfile, UserProfileAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
