# Generated by Django 4.0 on 2022-06-04 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_equipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='image1',
            field=models.ImageField(default='', upload_to='mainapp/images'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='image2',
            field=models.ImageField(default='', upload_to='mainapp/images'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='image3',
            field=models.ImageField(default='', upload_to='mainapp/images'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='image4',
            field=models.ImageField(default='', upload_to='mainapp/images'),
        ),
    ]
