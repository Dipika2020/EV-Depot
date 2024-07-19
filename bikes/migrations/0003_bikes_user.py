# Generated by Django 5.0.6 on 2024-07-19 02:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0002_alter_bikes_createdat'),
        ('users', '0008_remove_buyer_gender_remove_buyer_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikes',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bikes', to='users.buyer'),
        ),
    ]