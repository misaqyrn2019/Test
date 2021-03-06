# Generated by Django 3.2.5 on 2021-09-29 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FacilitiesWelfare', '0019_auto_20210929_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeHelp',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='شناسه')),
                ('Title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('TypeAssistance', models.CharField(choices=[('MA', 'ازدواج'), ('BG', 'هدیه تولد'), ('NC', 'فرزند جدید'), ('AN', 'غیره')], default='AN', max_length=2, verbose_name='نوع')),
                ('DateRegister', models.DateTimeField(verbose_name='تاریخ ثبت')),
                ('Description', models.TextField(verbose_name='توضیحات')),
                ('IdUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'کمک بلاعوض',
                'verbose_name_plural': 'کمک های بلاعوض',
            },
        ),
        migrations.RemoveField(
            model_name='registerassistance',
            name='IdAssistance',
        ),
        migrations.RemoveField(
            model_name='registerassistance',
            name='IdUser',
        ),
        migrations.DeleteModel(
            name='Assistance',
        ),
        migrations.DeleteModel(
            name='RegisterAssistance',
        ),
    ]
