# Generated by Django 2.1.7 on 2020-12-17 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gr33kLibrary', '0010_auto_20201217_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='upload_user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gr33kLibrary.User'),
        ),
    ]
