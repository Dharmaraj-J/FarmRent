# Generated by Django 4.0 on 2022-06-05 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_equipment_equipmentholder_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests_apply',
            name='request_status',
            field=models.CharField(default='Pending', max_length=75),
        ),
    ]
