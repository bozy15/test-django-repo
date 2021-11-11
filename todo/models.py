from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    complete = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return str(self.name)
