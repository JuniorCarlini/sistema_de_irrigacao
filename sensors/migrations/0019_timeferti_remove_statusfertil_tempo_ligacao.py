# Generated by Django 5.1.1 on 2024-10-17 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sensors", "0018_statusfertil_tempo_ligacao"),
    ]

    operations = [
        migrations.CreateModel(
            name="TimeFerti",
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
                ("time_ferti_ms", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name="statusfertil",
            name="tempo_ligacao",
        ),
    ]