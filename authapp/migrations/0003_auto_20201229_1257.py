# Generated by Django 3.1.4 on 2020-12-29 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20201229_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='smartphone',
            field=models.BooleanField(default=True),
        ),
    ]