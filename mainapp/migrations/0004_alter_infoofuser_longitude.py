# Generated by Django 4.0 on 2022-06-02 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_infoofuser_latitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoofuser',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
