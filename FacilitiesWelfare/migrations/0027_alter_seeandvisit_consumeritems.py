# Generated by Django 3.2.5 on 2021-09-30 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacilitiesWelfare', '0026_auto_20210930_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seeandvisit',
            name='ConsumerItems',
            field=models.CharField(choices=[('F', 'پدر'), ('M', 'مادر'), ('B', 'برادر'), ('S', 'خواهر'), ('D', 'دایی'), ('A', 'عمو'), ('K', 'خاله'), ('E', 'عمه')], max_length=2, verbose_name='نسبت'),
        ),
    ]
