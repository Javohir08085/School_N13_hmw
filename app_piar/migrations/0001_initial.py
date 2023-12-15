# Generated by Django 4.2.7 on 2023-12-07 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title_uz', models.CharField(max_length=300, verbose_name='Yangilik sarlavhasi')),
                ('news_title_en', models.CharField(max_length=300, verbose_name='News title')),
                ('news_title_ru', models.CharField(max_length=300, verbose_name='Заголовок новости')),
                ('news_image', models.ImageField(blank=True, null=True, upload_to='images/news', verbose_name='Image')),
                ('news_desc_uz', models.CharField(max_length=500, verbose_name='Yangilik qisqacha tavsifi')),
                ('news_desc_en', models.CharField(blank=True, max_length=500, null=True, verbose_name='News description')),
                ('news_desc_ru', models.CharField(blank=True, max_length=500, null=True, verbose_name='Описание новости')),
                ('news_text_uz', models.TextField(verbose_name='Yangilik to‘liq matni')),
                ('news_text_en', models.TextField(blank=True, null=True, verbose_name='News full text')),
                ('news_text_ru', models.TextField(blank=True, null=True, verbose_name='Текст новости')),
                ('news_datetime', models.DateTimeField(auto_now_add=True)),
                ('news_views_count', models.IntegerField(default=0, verbose_name='Ko‘rishlar soni')),
                ('news_source', models.URLField(blank=True, null=True, verbose_name='Manba (agar mavjud bo‘lsa)')),
            ],
            options={
                'db_table': 'pr_news',
                'ordering': ('news_datetime',),
            },
        ),
    ]
