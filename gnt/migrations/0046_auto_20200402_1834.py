# Generated by Django 3.0.3 on 2020-04-02 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gnt', '0045_downvoteduserdrink_upvoteduserdrink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdrink',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]
