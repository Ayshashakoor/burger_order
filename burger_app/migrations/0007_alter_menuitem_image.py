# Generated by Django 5.1 on 2024-09-22 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger_app', '0006_alter_menuitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(upload_to='static/img/burger'),
        ),
    ]
