from django.contrib import admin
/home/javohir/Desktop/School_N13
from django.contrib.admin import ModelAdmin

from .models import Subject


@admin.register(Subject)
class SubjectAdmin(ModelAdmin):
    fields = ['subject_name_uz','subject_name_en','subject_name_ru',
              'theme_title_uz','theme_title_en','theme_title_ru',
              'subject_start_time','subject_end_time']



