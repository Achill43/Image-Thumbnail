from django.db import models


class Category(models.Model):
    name = models.CharField("Name", max_length=30)
    description = models.TextField()
    slug = models.SlugField(max_length=160, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Genre(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=160, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return  self.name


class Author(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='img/authors/')
    slug = models.SlugField(max_length=160, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    slug = models.SlugField(max_length=160, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"


class Book(models.Model):
    name = models.CharField("Book", max_length=50)
    show = models.BooleanField("Show", default=True)
    previesImg = models.ImageField(upload_to='img/books/')
    description = models.TextField()
    price = models.DecimalField("Price", max_digits=5, decimal_places=2)
    author = models.ManyToManyField(Author, verbose_name='Authors', related_name="book_author")
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category, verbose_name='Categories', related_name="book_category")
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=160, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updeted_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = "Books"
