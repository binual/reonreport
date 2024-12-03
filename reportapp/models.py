from django.db import models

class Activity(models.Model):
    date = models.DateField()
    client = models.CharField(max_length=255)
    activity = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('in-progress', 'In Progress'), ('completed', 'Completed')],
    )

    def __str__(self):
        return f"{self.client} - {self.activity}"
