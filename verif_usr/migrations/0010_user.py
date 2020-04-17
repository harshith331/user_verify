# Generated by Django 3.0.2 on 2020-04-17 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('verif_usr', '0009_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('last_name', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('date_of_birth', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('country_of_residence', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('state', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('city_of_residence', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('phone_no', models.CharField(default='', max_length=15)),
                ('fav_gnr_writing', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('password', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('ready', models.BooleanField(default=False)),
                ('doc_url', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('otp', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('short_story', models.TextField(default='')),
            ],
        ),
    ]