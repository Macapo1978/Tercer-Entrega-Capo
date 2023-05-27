# Generated by Django 4.2.1 on 2023-05-27 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=250)),
                ('requisitos', models.CharField(max_length=250)),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('apelido', models.CharField(max_length=150)),
                ('edad', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('mail', models.CharField(max_length=250)),
                ('excursion_comprada_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='excursion.excursion')),
                ('formadepago_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='excursion.formapago')),
            ],
        ),
    ]
