# Generated by Django 5.0.2 on 2024-03-03 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsa', '0003_usercode_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variable_type', models.CharField(blank=True, max_length=50, null=True)),
                ('variable1', models.CharField(blank=True, max_length=50, null=True)),
                ('variable2', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]