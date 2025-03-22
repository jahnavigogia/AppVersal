from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime
import re


def validate_date_format(value):
    """Validator to check if the date is in DD/MM/YYYY format."""
    try:
        datetime.datetime.strptime(value, "%d/%m/%Y")
    except ValueError:
        raise ValidationError("Date must be in DD/MM/YYYY format.")


def validate_username(username):
    """Validate to check username(if enetered) contains special symbols"""
    if username and re.match(r"^[a-zA-Z0-9_]+_+[a-zA-Z0-9_]", username):
        raise ValidationError(
            "Username can only contain letters, numbers, and underscores."
        )


# Create your models here.
class User(models.Model):
    """Model for user details"""

    id = models.IntegerField
    username = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True,
        validators=[validate_username],
    )
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    # date_joined = models.CharField(
    #     max_length=10, validators=[validate_date_format], null=True
    # )
    date_joined = models.DateField(
        null=True, blank=True, help_text="Format should be DD/MM/YYYY"
    )
    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name="customuser_set", blank=True
    )

    def save(self, *args, **kwargs):
        """Ensure first letter of first_name and last_name is uppercase before saving."""
        if self.first_name:
            self.first_name = self.first_name.capitalize()
        if self.last_name:
            self.last_name = self.last_name.capitalize()
        super().save(*args, **kwargs)
