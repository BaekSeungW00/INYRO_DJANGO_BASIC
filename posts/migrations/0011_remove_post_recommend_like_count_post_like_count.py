# Generated by Django 4.2.5 on 2023-11-28 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_post_recommend_like_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_recommend',
            name='like_count',
        ),
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
