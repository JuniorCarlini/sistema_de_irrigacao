# Generated by Django 5.1.1 on 2024-10-17 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sensors", "0014_remove_datafertil_start_feril"),
    ]

    operations = [
        migrations.AddField(
            model_name="datafertil",
            name="start_fertil",
            field=models.BooleanField(default=False),
        ),
    ]
