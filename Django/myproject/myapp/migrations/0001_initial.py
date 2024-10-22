# Generated by Django 5.1.2 on 2024-10-14 05:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChaVarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('cha_type', models.CharField(choices=[('ML', 'Milk Tea'), ('BL', 'Black Tea'), ('GR', 'Green Tea'), ('EL', 'Earl Grey Tea')], default='ML', max_length=2)),
            ],
        ),
    ]