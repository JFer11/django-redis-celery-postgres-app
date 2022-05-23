# Generated by Django 2.2.28 on 2022-05-23 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('lote', models.CharField(max_length=128)),
                ('cantidad_disponible', models.IntegerField()),
                ('fecha_de_vencimiento', models.DateTimeField()),
                ('cantidad_minima_del_medicamento', models.IntegerField()),
                ('notificacion_previa_al_vencimiento', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_dose',
        ),
        migrations.RemoveField(
            model_name='user',
            name='had_covid',
        ),
        migrations.RemoveField(
            model_name='user',
            name='second_dose',
        ),
        migrations.RemoveField(
            model_name='user',
            name='vaccinated',
        ),
        migrations.AlterField(
            model_name='user',
            name='document',
            field=models.CharField(max_length=9, unique=True),
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
        migrations.DeleteModel(
            name='VaccinationCenter',
        ),
    ]
