# Generated by Django 4.2.14 on 2024-07-14 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_customuser_address_remove_customuser_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='abc@gmail.com', max_length=254),
        ),
    ]
