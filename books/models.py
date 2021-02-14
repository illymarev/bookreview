from django.db import models


# Create your models here.


class BookModel(models.Model):
    title = models.CharField(max_length=256, unique=True)
    author = models.CharField(max_length=256)
    genre = models.CharField(max_length=256)
    description = models.TextField()
    my_review = models.TextField()
    release_year = models.PositiveIntegerField(default=0)
    length = models.PositiveIntegerField()
    photo = models.ImageField(blank=False, upload_to='static/images')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=256)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Comment {self.text} by {self.name}'


class Quote(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='quotes')
    text = models.TextField()
    author = models.CharField(max_length=256, default=None)

    def __str__(self):
        return self.text