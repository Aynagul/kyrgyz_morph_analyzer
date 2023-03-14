from django.db import models
from ckeditor.fields import RichTextField

class About(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    text = models.TextField(blank=True, verbose_name='Текст статьи')

    def __str__(self):
        return self.title

from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=150)
    description = RichTextField()
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.tag)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tag


class PartOfSpeech(models.Model):
    id = models.AutoField(primary_key=True)
    part_of_speech = models.CharField(max_length=150)
    description = RichTextField()
    tag = models.ManyToManyField(Tags, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.part_of_speech)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.part_of_speech


class AllRoot(models.Model):
    root = models.CharField(max_length=150)
    part_of_speech = models.ForeignKey(PartOfSpeech, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.root)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.root}"


class NewRoot(models.Model):
    word = models.CharField(max_length=150)
    tags = models.CharField(max_length=150)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.word}"