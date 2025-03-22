# Generated by Django 5.1.7 on 2025-03-22 22:20

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_alter_user_date_joined"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                unique=True,
                validators=[users.models.validate_username],
            ),
        ),
    ]
