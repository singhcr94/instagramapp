# Generated by Django 2.1.1 on 2018-10-03 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20181002_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='postpics',
            field=models.ImageField(blank=True, null=True, upload_to='postpic'),
        ),
        migrations.AlterField(
            model_name='image',
            name='profilepic',
            field=models.ImageField(blank=True, null=True, upload_to='profilepic'),
        ),
    ]
