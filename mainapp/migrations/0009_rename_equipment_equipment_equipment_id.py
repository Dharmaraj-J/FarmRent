# Generated by Django 4.0 on 2022-06-04 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_equipment_equipment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment',
            old_name='equipment',
            new_name='equipment_id',
        ),
    ]