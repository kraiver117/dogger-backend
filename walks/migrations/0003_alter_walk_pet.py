# Generated by Django 3.2.5 on 2021-07-14 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_alter_pet_user'),
        ('walks', '0002_auto_20210714_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walk',
            name='pet',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pets.pet'),
        ),
    ]
