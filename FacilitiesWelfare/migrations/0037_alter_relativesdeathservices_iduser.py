# Generated by Django 3.2.5 on 2021-11-12 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0004_auto_20211105_1833'),
        ('FacilitiesWelfare', '0036_alter_reward_iduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relativesdeathservices',
            name='IdUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR.personnel', verbose_name='پرسنل'),
        ),
    ]