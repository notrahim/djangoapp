# models.py

from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)  # Ensures that each email is only used once

    def __str__(self):
        return self.email