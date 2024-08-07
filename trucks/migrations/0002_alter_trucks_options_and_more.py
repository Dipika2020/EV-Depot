# Generated by Django 5.0.6 on 2024-07-20 18:10

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0001_initial'),
        ('users', '0008_remove_buyer_gender_remove_buyer_state'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trucks',
            options={},
        ),
        migrations.RenameField(
            model_name='trucks',
            old_name='company_name',
            new_name='companyName',
        ),
        migrations.RenameField(
            model_name='trucks',
            old_name='is_new',
            new_name='isNew',
        ),
        migrations.RenameField(
            model_name='trucks',
            old_name='manufacturing_year',
            new_name='manufacturingYear',
        ),
        migrations.RenameField(
            model_name='trucks',
            old_name='model_type',
            new_name='modelType',
        ),
        migrations.RemoveField(
            model_name='trucks',
            name='created_at',
        ),
        migrations.AddField(
            model_name='trucks',
            name='createdAt',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='trucks',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='trucks', to='users.buyer'),
        ),
        migrations.AlterField(
            model_name='trucks',
            name='image',
            field=models.ImageField(upload_to='trucks/'),
        ),
    ]
