from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MovieList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Reviews(models.Model):
    movie = models.ForeignKey(MovieList, on_delete=models.CASCADE,
                               related_name="reviews") #ForeignKey karon ekta movie er multiple review thakte pare
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f"Review by {self.reviewer} on {self.movie}"