# Generated by Django 4.1.2 on 2022-10-08 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artillery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('type', models.CharField(max_length=70)),
                ('caliber', models.IntegerField()),
                ('range', models.IntegerField()),
                ('crew', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BWP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('speed', models.IntegerField()),
                ('caliber', models.IntegerField()),
                ('armor', models.IntegerField()),
                ('crew', models.IntegerField()),
                ('rate_of_fire', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('speed', models.IntegerField()),
                ('caliber', models.IntegerField()),
                ('crew', models.IntegerField(default=1)),
                ('other_weapons', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('speed', models.IntegerField()),
                ('caliber', models.IntegerField()),
                ('armor', models.IntegerField()),
                ('crew', models.IntegerField(default=1)),
                ('rate_of_fire', models.IntegerField(default=4)),
            ],
        ),
        migrations.CreateModel(
            name='Warship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('speed', models.IntegerField()),
                ('caliber', models.IntegerField()),
                ('armor', models.IntegerField()),
                ('crew', models.IntegerField()),
                ('rate_of_fire', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('other_weapons', models.CharField(max_length=200)),
            ],
        ),
    ]
