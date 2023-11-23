from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


def valideCin(value):
    if len(value) != 8:
        raise ValidationError(message="Cin must has 8 characters !")
    return value

def validateEmail(value):
    validateReg = "@esprit.tn"
    if not str(value).endswith(validateReg):
        raise ValidationError(f"Your name {value} doesn't end with {validateReg}!")
    return value


# Create your models here.
class Person(AbstractUser):
    cin = models.CharField(primary_key=True, max_length=8, validators=[valideCin])
    email = models.EmailField(max_length=50, validators=[validateEmail])
    username = models.CharField(max_length=24, unique=True)

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = "Person"

    def __str__(self):
        return self.username
