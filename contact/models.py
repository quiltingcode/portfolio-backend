from django.db import models


class Contact(models.Model):
    """
    Contact model
    """
    name = models.CharField(max_length=100, blank=False)
    company = models.CharField(max_length=255, blank=True)
    message = models.TextField(max_length=255)
    email = models.EmailField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner} : {self.message}"
