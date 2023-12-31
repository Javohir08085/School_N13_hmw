# Generated by Django 4.2.7 on 2023-12-13 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BestTeachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_fullname_uz', models.CharField(max_length=50, verbose_name="O'qituvchi ismi familiyasi")),
                ('teacher_fullname_en', models.CharField(max_length=50, verbose_name='Teacher fullname')),
                ('teacher_fullname_ru', models.CharField(max_length=50, verbose_name='Имя и фамилия учителя')),
                ('teacher_specialty_uz', models.CharField(max_length=50, verbose_name="O'qituvchi mutaxassislik fani")),
                ('teacher_specialty_en', models.CharField(max_length=50, verbose_name='Teacher specialty')),
                ('teacher_specialty_ru', models.CharField(max_length=50, verbose_name='Специальность учителя')),
                ('teacher_phone', models.CharField(max_length=20, verbose_name="O'qituvchi telefon raqami")),
            ],
            options={
                'db_table': 'teacher_infos',
            },
        ),
    ]
