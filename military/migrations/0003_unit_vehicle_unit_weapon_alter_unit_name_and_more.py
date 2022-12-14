# Generated by Django 4.1.2 on 2022-10-11 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('military', '0002_crew_unit_unittype_vechicle_weapon_delete_artillery_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='vehicle',
            field=models.ManyToManyField(to='military.vechicle'),
        ),
        migrations.AddField(
            model_name='unit',
            name='weapon',
            field=models.ManyToManyField(to='military.weapon'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(max_length=125),
        ),
        migrations.AlterField(
            model_name='unittype',
            name='name',
            field=models.CharField(max_length=125),
        ),
    ]
