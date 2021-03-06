# Generated by Django 3.2.5 on 2021-10-07 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0018_auto_20211008_0059'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldofStudy',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Title', models.CharField(max_length=100, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'رشته تحصیلی',
                'verbose_name_plural': 'رشته تحصیلی',
            },
        ),
        migrations.CreateModel(
            name='GradeofStudy',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Title', models.CharField(max_length=100, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'مقطع تحصیلی',
                'verbose_name_plural': 'مقطع تحصیلی',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Title', models.CharField(max_length=100, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'گروه',
                'verbose_name_plural': 'گروه',
            },
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('NumberPersonnel', models.IntegerField(max_length=10, unique=True, verbose_name='شماره پرسنلی')),
                ('Name', models.CharField(max_length=100, verbose_name='نام')),
                ('Family', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('DateBirthDay', models.DateField(verbose_name='تاریخ تولد')),
                ('Address', models.TextField(verbose_name='آدرس')),
                ('NationalCode', models.CharField(max_length=10, verbose_name='کد ملی')),
                ('IdCode', models.CharField(max_length=10, verbose_name='شماره شناسنامه')),
                ('IdNumber', models.CharField(max_length=10, verbose_name='شماره شناسنامه')),
                ('HomePhoneNumber', models.CharField(max_length=10, verbose_name='شماره منزل')),
                ('MobileNumber', models.CharField(max_length=10, verbose_name='شماره همراه')),
                ('EmergencyNumber', models.CharField(max_length=10, verbose_name='شماره اضطراری')),
                ('Email', models.EmailField(max_length=50, verbose_name='ایمیل')),
                ('UserName', models.CharField(max_length=50, verbose_name='نام کاربری')),
                ('Password', models.CharField(max_length=50, verbose_name='رمز عبور')),
                ('DateMarried', models.DateField(verbose_name='تاریخ ازدواج')),
                ('RegisterDateTime', models.DateTimeField(auto_now=True, verbose_name='تاریخ ثبت')),
                ('Gender', models.CharField(choices=[('M', 'مذکر'), ('F', 'مونث')], default='M', max_length=1, verbose_name='جنسیت')),
                ('MaritalStatus', models.CharField(choices=[('N', 'مجرد'), ('Y', 'متاهل')], default='Y', max_length=1, verbose_name='وضعیت تاهل')),
                ('IsActive', models.CharField(choices=[('Y', 'فعال'), ('N', 'غیرفعال')], default='Y', max_length=1, verbose_name='فعال')),
                ('IdCity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.city', verbose_name='نام شهرستان')),
                ('IdFieldofStudy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR.fieldofstudy', verbose_name='رشته تحصیلی')),
                ('IdGradeofStudy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR.gradeofstudy', verbose_name='مقطع تحصیلی')),
                ('IdGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR.group', verbose_name='گروه')),
            ],
            options={
                'verbose_name': 'کاربران',
                'verbose_name_plural': 'کاربران',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Title', models.CharField(max_length=100, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'سمت',
                'verbose_name_plural': 'سمت',
            },
        ),
        migrations.CreateModel(
            name='ProfileofChildren',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Name', models.CharField(max_length=100, verbose_name='نام')),
                ('Family', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('Gender', models.CharField(choices=[('M', 'مذکر'), ('F', 'مونث')], default='M', max_length=1, verbose_name='جنسیت')),
                ('NationalCode', models.CharField(max_length=10, verbose_name='کد ملی')),
                ('BirthDate', models.DateField(verbose_name='تاریخ تولد')),
                ('IdPersonnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR.personnel', verbose_name='پرسنل')),
            ],
            options={
                'verbose_name': 'پرسنل',
                'verbose_name_plural': 'پرسنل',
            },
        ),
        migrations.AddField(
            model_name='personnel',
            name='IdPost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR.post', verbose_name='سمت'),
        ),
        migrations.AddField(
            model_name='personnel',
            name='IdProvince',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.province', verbose_name='نام استان'),
        ),
    ]
