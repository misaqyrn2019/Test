# Generated by Django 3.2.5 on 2021-09-29 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacilitiesWelfare', '0013_cashassistance_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashassistance',
            name='DateRegister',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='cashassistance',
            name='Price',
            field=models.IntegerField(default=0, verbose_name='مبلغ کمک'),
        ),
        migrations.AlterField(
            model_name='cashassistance',
            name='TypeAssistance',
            field=models.CharField(choices=[('PU', 'همگانی'), ('PR', 'خاص'), ('N', 'انتخاب نشده')], default='N', max_length=2, verbose_name='نوع کمک'),
        ),
    ]
