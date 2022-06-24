from django.db import models


class djangoClasses(models.Model):
    Title = models.CharField(max_length=100)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=60)
    #Duration in hours
    Duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.Title
