# Generated by Django 5.0 on 2023-12-07 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Books",
            fields=[
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("Id", models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]