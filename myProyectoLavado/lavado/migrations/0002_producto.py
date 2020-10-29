# Generated by Django 2.2.16 on 2020-10-28 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lavado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('nombre', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
