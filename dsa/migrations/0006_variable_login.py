# Generated by Django 5.0.2 on 2024-03-03 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsa', '0005_variable_user_var'),
    ]

    operations = [
        migrations.AddField(
            model_name='variable',
            name='login',
            field=models.BooleanField(default=False),
        ),
    ]
