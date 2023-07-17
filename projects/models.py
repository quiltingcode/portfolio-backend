from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, default='project')
    description = models.TextField(blank=True, default='a brilliant project')
    tech_stack = TaggableManager(
        help_text='A comma-separated list of tags',
        blank=True,
        verbose_name='tech stack used'
    )
    image = models.ImageField(
        upload_to='images/', default='../profile-pic_nfhakf'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s {self.title}"
