# Generated by Django 4.2.16 on 2024-11-26 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_searchcoin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchcoin',
            name='name',
        ),
    ]
