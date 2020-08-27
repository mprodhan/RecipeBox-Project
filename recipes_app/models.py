from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)
    # User = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    instructions = models.TextField()
    time_required = models.CharField(max_length=20)
    image = models.ImageField(upload_to='img', null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
