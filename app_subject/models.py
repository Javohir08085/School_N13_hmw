from django.db import models

class Subject(models.Model):
    subject_name_uz = models.CharField(max_length=50,verbose_name='Fan nomi')
    subject_name_en = models.CharField(max_length=50,verbose_name='Subject name')
    subject_name_ru = models.CharField(max_length=50,verbose_name='Урок имя')
    theme_title_uz = models.CharField(max_length=255,verbose_name='Mavzu sarlavhasi')
    theme_title_en = models.CharField(max_length=255,verbose_name='Theme title')
    theme_title_ru = models.CharField(max_length=255,verbose_name='Название темы')
    subject_start_time = models.DateTimeField(verbose_name='Boshlanish vaqti')
    subject_end_time = models.DateTimeField(verbose_name='Tugash vaqti')

    def __str__(self):
        return self.subject_name_uz

    class Meta:
        db_table = 'subject'
