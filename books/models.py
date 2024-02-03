import uuid  # new
from django.contrib.auth import get_user_model  # new
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=100)
    icon_path = models.CharField(max_length=255, help_text="Relative path to the static icon")

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    url_link = models.URLField(max_length=200, blank=True)
    client = models.CharField(max_length=200, blank=True)
    details = models.TextField(blank=True)
    technologies = models.ManyToManyField(Technology, related_name='books', blank=True)

    class Meta: 
        indexes = [
            models.Index(fields=['id'], name='id_index'),
        ]
        permissions = [
            ('special_status', 'Can read all books'),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])


class Review(models.Model):  # new
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review