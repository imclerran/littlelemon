# Generated by Django 5.0.2 on 2024-02-27 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menu_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
