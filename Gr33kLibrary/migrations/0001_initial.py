# Generated by Django 2.1.7 on 2020-12-15 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('is_lock', models.BooleanField(default=False)),
                ('login_fail', models.IntegerField(default=0)),
                ('invitation_code', models.CharField(max_length=255, null=True)),
                ('invitation_user', models.IntegerField(null=True)),
            ],
        ),
    ]
