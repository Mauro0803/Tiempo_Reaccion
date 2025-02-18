# Generated by Django 5.0.7 on 2024-07-25 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tiempo",
            fields=[
                ("prueba_id", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=64)),
                ("letra_1", models.CharField(max_length=1)),
                ("tiempo_1", models.DecimalField(decimal_places=10, max_digits=15)),
                ("letra_2", models.CharField(max_length=1)),
                ("tiempo_2", models.DecimalField(decimal_places=10, max_digits=15)),
                ("letra_3", models.CharField(max_length=1)),
                ("tiempo_3", models.DecimalField(decimal_places=10, max_digits=15)),
                ("letra_4", models.CharField(max_length=1)),
                ("tiempo_4", models.DecimalField(decimal_places=10, max_digits=15)),
                ("letra_5", models.CharField(max_length=1)),
                ("tiempo_5", models.DecimalField(decimal_places=10, max_digits=15)),
            ],
        ),
    ]
