# Generated by Django 3.2.5 on 2021-07-14 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('walkers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('walks', '0004_alter_walk_pet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walk',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='walk',
            name='walker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='walkers.walker'),
        ),
    ]
