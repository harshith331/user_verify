# Generated by Django 3.0.2 on 2020-04-17 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verif_usr', '0010_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='registered',
            field=models.BooleanField(default=False),
        ),
    ]
