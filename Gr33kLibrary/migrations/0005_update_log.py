# Generated by Django 2.1.7 on 2020-12-16 15:20

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Gr33kLibrary', '0004_auto_20201216_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update_log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('content', mdeditor.fields.MDTextField()),
            ],
        ),
    ]
