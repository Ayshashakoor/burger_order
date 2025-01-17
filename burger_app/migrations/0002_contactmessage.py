# Generated by Django 5.1 on 2024-09-21 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(default='No subject', max_length=200)),
                ('message', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
