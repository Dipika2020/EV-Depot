# Generated by Django 4.2.14 on 2024-07-14 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='password',
            field=models.CharField(default='abc', max_length=30),
        ),
    ]
