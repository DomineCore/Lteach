# Generated by Django 3.2.8 on 2022-03-13 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guardian', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='学生姓名')),
                ('birth', models.DateField(verbose_name='出生日期')),
                ('address', models.CharField(max_length=255, verbose_name='家庭住址')),
                ('guardian', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='guardian.guardian', verbose_name='监护人')),
            ],
        ),
    ]