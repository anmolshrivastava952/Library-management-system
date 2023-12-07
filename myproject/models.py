from django.db import models

class Books(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    Id=models.AutoField(primary_key=True)

    def __str__(self):
        return self.title
    
