# Generated by Django 3.2.5 on 2021-07-15 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_alter_pet_user'),
        ('walks', '0007_alter_walk_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walk',
            name='pet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pets.pet'),
        ),
    ]