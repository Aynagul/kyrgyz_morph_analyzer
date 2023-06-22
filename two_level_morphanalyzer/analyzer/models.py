from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Tags(models.Model):
    SEMESTER_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
    )
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=150)
    priority = models.CharField(max_length=100, choices=SEMESTER_CHOICES)
    description = RichTextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.tag)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Тегдер'
        ordering = ['id']


class Endings(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    tagid = models.ForeignKey(Tags, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мүчө'
        verbose_name_plural = 'Мүчөлөр'
        ordering = ['id']


class PartOfSpeech(models.Model):
    id = models.AutoField(primary_key=True)
    part_of_speech = models.CharField(max_length=150)
    description = RichTextField()
    tag = models.ManyToManyField(Tags)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.part_of_speech)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.part_of_speech

    class Meta:
        verbose_name = 'Сөз түркүмү'
        verbose_name_plural = 'Сөз түркүмдөрү'
        ordering = ['id']


class AllRoot(models.Model):
    root = models.CharField(max_length=150)
    part_of_speech = models.ForeignKey(PartOfSpeech, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tags, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.root)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.root}"

    class Meta:
        verbose_name = 'Негиз'
        verbose_name_plural = 'Негиздер'
        ordering = ['id']


class NewRoot(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=150)
    root = models.CharField(max_length=150)
    tags = models.CharField(max_length=150)
    endings = models.CharField(max_length=150,null=True)
    is_done = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Жаңы негиз'
        verbose_name_plural = 'Жаңы негиздер'
        ordering = ['id']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.word)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.word}"

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return self.name
