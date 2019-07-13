from django.db import models
from datetime import datetime

class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length=200)
    

# Create your models here.
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published", default=datetime.now)

    def __str__(self):
        return self.tutorial_title