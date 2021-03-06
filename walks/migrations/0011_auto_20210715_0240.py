# Generated by Django 3.2.5 on 2021-07-15 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_alter_pet_user'),
        ('walkers', '0001_initial'),
        ('walks', '0010_auto_20210715_0238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='walk',
            name='pet',
        ),
        migrations.AddField(
            model_name='walk',
            name='pet',
            field=models.ManyToManyField(to='pets.Pet'),
        ),
        migrations.RemoveField(
            model_name='walk',
            name='walker',
        ),
        migrations.AddField(
            model_name='walk',
            name='walker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='walkers.walker'),
        ),
    ]
