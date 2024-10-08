# Generated by Django 5.0.6 on 2024-08-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("OrcaBlogsWebsite", "0002_blogpost_blogid"),
    ]

    operations = [
        migrations.CreateModel(
            name="PostComment",
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
                ("Name", models.CharField(default="", max_length=100)),
                ("Email", models.CharField(default="", max_length=100)),
                ("Message", models.CharField(default="", max_length=10000)),
                ("Date", models.CharField(default="", max_length=100)),
            ],
        ),
    ]
