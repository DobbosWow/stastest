# Generated by Django 2.1.5 on 2019-02-06 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegNewUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=40)),
                ('userPass', models.CharField(max_length=20)),
            ],
        ),
    ]
