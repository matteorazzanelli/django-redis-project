# Generated by Django 4.0.3 on 2022-03-08 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bacheca', '0004_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]