# Generated by Django 4.0 on 2022-06-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_equipment_company_equipment_old'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='equipment',
            field=models.IntegerField(null=True),
        ),
    ]
