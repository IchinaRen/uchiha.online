# Generated by Django 2.2 on 2019-07-24 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myaccount', '0002_auto_20190724_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='昵称'),
        ),
    ]
