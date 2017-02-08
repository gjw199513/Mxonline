# -*- coding:utf-8 -*-
__author__ = 'gjw'
__date__ = '2017/1/14 19:31'

from .models import Course, Lesson , Video, CourseResource, BannerCourse
import xadmin
from organization.models import CourseOrg


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


# 课程注册
class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students',
                    'fav_nums', 'click_nums', 'add_time', 'get_zj_nums', 'go_to']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students', 'fav_nums', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'click_nums', 'add_time']
    ordering = ['-click_nums']
    readonly_fields = ['fav_nums']
    list_editable = ['degree', 'desc']
    exclude = ['click_nums']
    inlines = [LessonInline, CourseResourceInline]
    # refresh_times = [3,5]
    style_fields = {"detail":"ueditor"}
    import_excel = True

    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        #在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

    def post(self, request, *args, **kwargs):
        if "excel" in request.FILES:
            pass
        return super(CourseAdmin, self).post(request, args, kwargs)


# 轮播课程注册
class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time','students','fav_nums','click_nums','add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students','fav_nums','click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time','students','fav_nums','click_nums','add_time']
    ordering = ['-click_nums']
    readonly_fields = ['fav_nums']
    exclude = ['click_nums']
    inlines = [LessonInline, CourseResourceInline]

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


# 章节注册
class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


# 视频注册
class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['lesson', 'name', 'add_time']


# 课程资源注册
class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)

