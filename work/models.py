from django.db import models
# Create your models here.


class Lists(models.Model):
    item = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item
