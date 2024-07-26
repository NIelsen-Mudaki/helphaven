from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"