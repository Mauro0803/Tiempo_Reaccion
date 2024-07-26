# Generated by Django 5.0.7 on 2024-07-26 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prueba",
            fields=[
                ("prueba_id", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=64)),
                ("letra_1", models.CharField(max_length=1)),
                ("tiempo_1", models.FloatField(default=0.0)),
                ("letra_2", models.CharField(max_length=1)),
                ("tiempo_2", models.FloatField(default=0.0)),
                ("letra_3", models.CharField(max_length=1)),
                ("tiempo_3", models.FloatField(default=0.0)),
                ("letra_4", models.CharField(max_length=1)),
                ("tiempo_4", models.FloatField(default=0.0)),
                ("letra_5", models.CharField(max_length=1)),
                ("tiempo_5", models.FloatField(default=0.0)),
            ],
        ),
        migrations.DeleteModel(
            name="Tiempo",
        ),
    ]
