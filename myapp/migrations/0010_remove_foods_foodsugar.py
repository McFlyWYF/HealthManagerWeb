# Generated by Django 2.1.2 on 2019-06-20 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_delete_eats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foods',
            name='foodSugar',
        ),
    ]
