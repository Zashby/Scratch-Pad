# Generated by Django 4.1 on 2022-08-24 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapr_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='users', to='mapr_app.group'),
        ),
    ]