# Generated by Django 3.0.1 on 2020-01-31 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to='user_avatars'),
        ),
    ]