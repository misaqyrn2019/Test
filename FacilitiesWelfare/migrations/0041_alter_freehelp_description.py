# Generated by Django 3.2.5 on 2021-12-03 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacilitiesWelfare', '0040_alter_freehelp_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freehelp',
            name='Description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
    ]
