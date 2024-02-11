from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically generated ID
    title = models.CharField(max_length=255)  # Required title
    author = models.CharField(max_length=255)  # Required author
    description = models.TextField(blank=True)  # Optional description
    isbn = models.CharField(max_length=50, unique=True)  # Required unique ISBN
    publication_date = models.DateField(blank=True, null=True)  # Optional publication date
    creation_date = models.DateTimeField(auto_now_add=True)  # Automatically generated creation date
    update_date = models.DateTimeField(auto_now=True)  # Automatically updated d

    def _str_(self):
        return self.title
# Create your models here.

# Create your models here.
