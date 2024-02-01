from django.contrib import admin
from .models import Book, Review, Category, Technology

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0  # Removes the extra empty forms at the bottom of the inline

class TechnologyInline(admin.TabularInline):
    model = Book.technologies.through  # This is the way to inline a ManyToMany field
    extra = 1

class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
        TechnologyInline,  # Add this to manage book technologies from the book admin
    ]
    list_display = ("title", "author", "price", "category", "publication_date", "client")  # Add your new fields here
    list_filter = ("category",)  # Optional: to filter books by category in the admin
    search_fields = ("title", "author", "client")  # Optional: to add a search box to the admin

    # If you want to customize the way the book form looks, you can use the fields attribute:
    fields = ("title", "author", "price", "cover", "category", "publication_date", "url_link", "client", "details")

admin.site.register(Book, BookAdmin)
admin.site.register(Category)  # Don't forget to register the new models
admin.site.register(Technology)
