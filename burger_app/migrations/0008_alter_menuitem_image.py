# Generated by Django 5.1 on 2024-09-22 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger_app', '0007_alter_menuitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.CharField(max_length=255),
        ),
    ]
