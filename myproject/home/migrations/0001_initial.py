# Generated by Django 5.0.2 on 2024-02-22 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mobiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('des', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='uploads/')),
                ('date', models.CharField(max_length=100)),
            ],
        ),
    ]
