# Generated by Django 3.2.6 on 2021-08-09 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieadmin', '0019_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Characters', to='movieadmin.book'),
        ),
    ]