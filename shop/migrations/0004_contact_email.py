# Generated by Django 3.2.3 on 2021-07-02 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
    ]
