# Generated by Django 4.1.4 on 2023-01-27 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='photo_avatar/'),
        ),
    ]