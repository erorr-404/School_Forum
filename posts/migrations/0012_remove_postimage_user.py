# Generated by Django 5.0.3 on 2024-03-25 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_category_thumb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postimage',
            name='user',
        ),
    ]
