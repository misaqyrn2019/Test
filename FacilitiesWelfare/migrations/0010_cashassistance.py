# Generated by Django 3.2.5 on 2021-09-29 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FacilitiesWelfare', '0009_auto_20210929_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashAssistance',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='شناسه')),
                ('TypeAssistance', models.CharField(choices=[('PU', 'همگانی'), ('PR', 'خاص')], default='N', max_length=2, verbose_name='نوع کمک')),
                ('Title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('Description', models.TextField(verbose_name='توضیحات')),
                ('IdUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='شناسه کاربر')),
            ],
            options={
                'verbose_name': 'کمک معیشتی نقدی',
                'verbose_name_plural': 'کمک های معیشتی',
            },
        ),
    ]
