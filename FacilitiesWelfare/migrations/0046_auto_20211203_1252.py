# Generated by Django 3.2.5 on 2021-12-03 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacilitiesWelfare', '0045_alter_freehelp_dateregister'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistance',
            name='Description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='cashassistance',
            name='Description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='consumeritems',
            name='Description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='Description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='organizationalhouse',
            name='Description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='organizationalhouse',
            name='Pelaque',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='پلاک'),
        ),
    ]
