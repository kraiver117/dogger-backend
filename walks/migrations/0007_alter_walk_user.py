# Generated by Django 3.2.5 on 2021-07-15 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210713_0345'),
        ('walks', '0006_auto_20210714_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walk',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]