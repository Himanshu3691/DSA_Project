# Generated by Django 5.0.2 on 2024-03-03 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsa', '0004_variable'),
    ]

    operations = [
        migrations.AddField(
            model_name='variable',
            name='user_var',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_var', to='dsa.user'),
        ),
    ]