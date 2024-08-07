# Generated by Django 5.0.6 on 2024-07-26 23:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0006_bikes_purchasedby'),
        ('users', '0011_buyer_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='bikes.bikes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.buyer')),
            ],
            options={
                'unique_together': {('bike', 'user')},
            },
        ),
    ]
