from django.contrib.auth.models import AbstractUser
from django.db import models
import random

class CustomUser(AbstractUser):
    confirmation_code = models.CharField(max_length=6, blank=True, null=True)
    is_active = models.BooleanField(default=False)  # Пользователь неактивен по умолчанию

    def generate_confirmation_code(self):
        self.confirmation_code = str(random.randint(100000, 999999))
        self.save()