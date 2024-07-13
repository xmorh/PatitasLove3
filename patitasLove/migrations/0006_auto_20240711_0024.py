# Generated by Django 3.1 on 2024-07-11 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patitasLove', '0005_auto_20240615_0357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VentaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patitasLove.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patitasLove.venta')),
            ],
        ),
        migrations.AddField(
            model_name='venta',
            name='productos',
            field=models.ManyToManyField(through='patitasLove.VentaProducto', to='patitasLove.Producto'),
        ),
    ]