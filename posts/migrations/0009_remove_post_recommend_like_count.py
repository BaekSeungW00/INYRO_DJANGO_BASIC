# Generated by Django 4.2.5 on 2023-11-28 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_post_recommend_like_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_recommend',
            name='like_count',
        ),
    ]