# Generated by Django 4.0 on 2022-06-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoofuser',
            name='latitude',
            field=models.FloatField(),
        ),
    ]
