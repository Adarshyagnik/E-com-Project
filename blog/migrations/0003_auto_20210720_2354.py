# Generated by Django 3.2.3 on 2021-07-20 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210720_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='chead0',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='chead1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='chead2',
        ),
    ]
