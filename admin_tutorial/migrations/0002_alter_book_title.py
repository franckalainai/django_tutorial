# Generated by Django 3.2.4 on 2021-10-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=36, unique=True),
        ),
    ]
