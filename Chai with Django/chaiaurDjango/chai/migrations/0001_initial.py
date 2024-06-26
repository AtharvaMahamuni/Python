# Generated by Django 5.0.6 on 2024-06-23 10:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChaiVarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='chais/')),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('chai_type', models.CharField(choices=[('ML', 'Masala'), ('KL', 'Kiwi'), ('GR', 'Ginger'), ('PL', 'Plain'), ('EL', 'Elaichi')], max_length=2)),
            ],
        ),
    ]
