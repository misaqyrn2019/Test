# Generated by Django 3.2.5 on 2021-09-28 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacilitiesWelfare', '0002_auto_20210928_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistance',
            name='DateExpire',
            field=models.DateTimeField(verbose_name='تاریخ انقضا'),
        ),
        migrations.AlterField(
            model_name='assistance',
            name='DateRegister',
            field=models.DateTimeField(verbose_name='تاریخ ثبت'),
        ),
    ]
