from django.db import models


# Create your models here.
class PostImage(models.Model):
    Title = models.CharField(max_length=500)
    Img = models.ImageField(upload_to='image/', blank=True)

    def __str__(self):
        return '{}'.format(self.Title)

    class Meta:
        verbose_name_plural = 'Posts'
