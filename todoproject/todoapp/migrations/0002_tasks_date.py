# Generated by Django 4.2.2 on 2023-07-10 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='date',
            field=models.DateField(default='1996-6-5'),
            preserve_default=False,
        ),
    ]
