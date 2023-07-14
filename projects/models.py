from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, default='project')
    description = models.TextField(blank=True, default='a brilliant project')
    tech_stack = models.CharField(max_length=255, blank=False, default='HTML')
    image = models.ImageField(
        upload_to='images/', default='../profile-pic_nfhakf'
    )
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s {self.title}"
