# Generated by Django 4.0.3 on 2022-03-15 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bacheca', '0013_post_hash_post_txid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hash',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='txId',
            field=models.CharField(blank=True, default=None, max_length=66, null=True),
        ),
    ]