# Generated by Django 4.2.5 on 2023-11-07 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_chatting_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatting',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chattings', to=settings.AUTH_USER_MODEL),
        ),
    ]
