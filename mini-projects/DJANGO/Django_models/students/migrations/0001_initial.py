# Generated by Django 4.0.6 on 2022-07-26 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('letter_grade', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], default='', max_length=1)),
                ('number_grade', models.FloatField(blank=True, null=True)),
                ('assignments', models.ManyToManyField(to='assignments.assignment')),
            ],
        ),
    ]