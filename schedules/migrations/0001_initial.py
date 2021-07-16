# Generated by Django 3.2.5 on 2021-07-15 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('walkers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beginning', models.TimeField()),
                ('end', models.TimeField()),
                ('day', models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo')], max_length=10)),
                ('size_dog', models.CharField(choices=[('Grande', 'Grande'), ('Mediano', 'Mediano'), ('Pequeño', 'Pequeño')], max_length=20)),
                ('walker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='walkers.walker')),
            ],
        ),
    ]
