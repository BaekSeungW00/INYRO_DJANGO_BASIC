# Generated by Django 4.2.5 on 2023-11-18 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='attachment',
            field=models.FileField(upload_to='post_attachment/'),
        ),
    ]
