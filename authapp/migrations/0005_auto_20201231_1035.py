# Generated by Django 3.1.4 on 2020-12-31 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20201231_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileimage',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authapp.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profileimage',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
