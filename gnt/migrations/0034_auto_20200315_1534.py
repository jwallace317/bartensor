# Generated by Django 3.0.3 on 2020-03-15 15:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gnt', '0033_auto_20200304_1840'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Drinks',
            new_name='Drink',
        ),
        migrations.RenameModel(
            old_name='Drink_names',
            new_name='DrinkName',
        ),
        migrations.RenameModel(
            old_name='Friend_request',
            new_name='FriendRequest',
        ),
        migrations.RenameModel(
            old_name='Profile_to_disliked_drink',
            new_name='ProfileToDislikedDrink',
        ),
        migrations.RenameModel(
            old_name='Profile_to_liked_drink',
            new_name='ProfileToLikedDrink',
        ),
        migrations.RenameModel(
            old_name='User_drink',
            new_name='UserDrink',
        ),
    ]