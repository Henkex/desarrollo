# Generated by Django 2.0.6 on 2018-06-22 23:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(blank=True, max_length=50, null=True)),
                ('capacidad', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Almacenes',
            },
        ),
        migrations.CreateModel(
            name='DetalleAlmacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'Detalle de almacen',
                'verbose_name_plural': 'Detalle de los almacenes',
            },
        ),
        migrations.CreateModel(
            name='DetalleIngreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.CharField(blank=True, max_length=20, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleSalida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Detalles de Salida',
                'verbose_name_plural': 'Detalles de Salidas',
            },
        ),
        migrations.CreateModel(
            name='DetalleStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
            },
        ),
        migrations.CreateModel(
            name='GuiaRemision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_traslado', models.DateField()),
                ('punto_partida', models.CharField(max_length=30)),
                ('nro_guia_remitente', models.CharField(max_length=15)),
                ('placa_vehiculo', models.CharField(max_length=10)),
                ('licencia_conducir', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Guias de remision',
            },
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('tipo', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Ingreso',
                'verbose_name_plural': 'Ingresos',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('ruc', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('nodo', models.CharField(blank=True, max_length=15, null=True)),
                ('devolucion', models.NullBooleanField()),
            ],
            options={
                'verbose_name': 'Salida',
                'verbose_name_plural': 'Salidas',
            },
        ),
    ]
