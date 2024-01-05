from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=1000)
    type = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    cast = models.CharField(max_length=700)
    country = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    listed_in = models.CharField(max_length=1000)
    description = models.CharField(max_length=1500)
    release_year = models.CharField(max_length=100)
    date_added = models.CharField(max_length=100)
    #updated_at = models.DateTimeField(auto_now=True)
    #creator = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


