# Generated by Django 5.1.1 on 2024-10-08 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sensors", "0007_remove_solenoidstate_water_used_waterusage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Configuracao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("token", models.CharField(max_length=255)),
            ],
        ),
    ]