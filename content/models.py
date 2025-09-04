from django.db import models

class HomeContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    hero_title = models.CharField(max_length=200)
    hero_subtitle = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class AboutContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
