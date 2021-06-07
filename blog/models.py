from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='blog/images/',blank=True)
    details = models.TextField()

    def __str__(self):
        return self.title

