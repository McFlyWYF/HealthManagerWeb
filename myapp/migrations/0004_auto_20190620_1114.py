# Generated by Django 2.2 on 2019-06-20 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190620_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eatstatistics',
            name='eatTime',
            field=models.DateField(max_length=100),
        ),
    ]
