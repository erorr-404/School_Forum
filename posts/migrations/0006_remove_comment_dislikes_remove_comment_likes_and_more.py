# Generated by Django 5.0.3 on 2024-03-19 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_commentlike_postlike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
