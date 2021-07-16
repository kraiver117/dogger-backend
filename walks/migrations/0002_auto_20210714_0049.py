# Generated by Django 3.2.5 on 2021-07-14 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='walk',
            old_name='accepted',
            new_name='is_accepted',
        ),
        migrations.AddField(
            model_name='walk',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]
