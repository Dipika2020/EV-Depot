# Generated by Django 5.0.6 on 2024-07-27 00:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0003_trucks_purchasedby_alter_trucks_user'),
        ('users', '0011_buyer_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='trucks.trucks')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.buyer')),
            ],
            options={
                'unique_together': {('truck', 'user')},
            },
        ),
    ]