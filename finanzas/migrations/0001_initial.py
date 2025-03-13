# Generated by Django 5.1.7 on 2025-03-13 16:12

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('limite', models.DecimalField(blank=True, decimal_places=2, help_text='Límite mensual para esta categoría (opcional)', max_digits=10, null=True)),
                ('icono', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(default='#0099ff', max_length=7)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorias', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['nombre'],
                'unique_together': {('nombre', 'usuario')},
            },
        ),
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moneda_preferida', models.CharField(choices=[('USD', 'Dólar estadounidense'), ('EUR', 'Euro'), ('MXN', 'Peso mexicano'), ('ARS', 'Peso argentino')], default='USD', help_text='Moneda en la que se mostrarán los valores por defecto', max_length=3)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('recibir_alertas_email', models.BooleanField(default=True, help_text='Recibir alertas por correo cuando se excedan los presupuestos')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo', models.CharField(choices=[('ingreso', 'Ingreso'), ('gasto', 'Gasto')], max_length=10)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('comprobante', models.FileField(blank=True, help_text='Recibo o comprobante de la transacción', null=True, upload_to='comprobantes/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transacciones', to='finanzas.categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transacciones', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transacción',
                'verbose_name_plural': 'Transacciones',
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_maximo', models.DecimalField(decimal_places=2, help_text='Cantidad máxima a gastar en esta categoría', max_digits=10)),
                ('mes', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], help_text='Mes del presupuesto (1-12)')),
                ('año', models.IntegerField(help_text='Año del presupuesto')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presupuestos', to='finanzas.categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presupuestos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Presupuesto',
                'verbose_name_plural': 'Presupuestos',
                'ordering': ['-año', '-mes', 'categoria__nombre'],
                'unique_together': {('usuario', 'categoria', 'mes', 'año')},
            },
        ),
    ]
