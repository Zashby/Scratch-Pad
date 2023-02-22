# Generated by Django 4.0.6 on 2022-07-26 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='people.state'),
            preserve_default=False,
        ),
    ]