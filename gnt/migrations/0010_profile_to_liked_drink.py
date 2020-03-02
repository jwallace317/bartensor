# Generated by Django 3.0.3 on 2020-03-01 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gnt', '0009_delete_profile_to_drink'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_to_liked_drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_FK', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gnt.Drinks')),
                ('profile_FK', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gnt.Profile')),
            ],
        ),
    ]
