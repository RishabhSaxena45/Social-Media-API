# Generated by Django 4.2.4 on 2024-04-21 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_friendrequest'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FriendRequest',
        ),
    ]