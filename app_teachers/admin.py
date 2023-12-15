from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import BestTeachers

@admin.register(BestTeachers)
class TeacherAdmin(ModelAdmin):
    fields = ['teacher_fullname_uz','teacher_fullname_en','teacher_fullname_ru',
              'teacher_specialty_uz','teacher_specialty_en','teacher_specialty_ru','teacher_phone']

    list_display = ['id','teacher_fullname_uz','teacher_specialty_uz']

# @admin.register(Subject)
# class SubjectAdmin(ModelAdmin):
#     fields = ['subject_name_uz','subject_name_en','subject_name_ru',
#               'theme_title_uz','theme_title_en','theme_title_ru',
#               'subject_start_time','subject_end_time']
#
#     list_display = ['id','subject_name_uz','theme_title_uz']