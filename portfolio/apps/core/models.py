from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Information(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=False)

    class Meta:
        ordering = ['-published_at']

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.is_public == False:
            is_public_text = "(非公開)"
        else:
            is_public_text = ""
        return '%s  %s' % (self.title, is_public_text)


class Work(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    production_year = models.IntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(2999)])
    content = models.TextField()
    used_tools = models.TextField()
    video_slug = models.SlugField(blank=True, null=True)
    thumbnail_1 = models.ImageField(upload_to='work_detail', blank=True, null=True)
    thumbnail_2 = models.ImageField(upload_to='work_detail', blank=True, null=True)
    thumbnail_3 = models.ImageField(upload_to='work_detail', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.is_public == False:
            is_public_text = "(非公開)"
        else:
            is_public_text = ""
        return '%s  %s' % (self.title, is_public_text)


class Cv(models.Model):

    class Genre(models.TextChoices):
        A_GROUP_EXHIBITION = 'グループ展',
        B_SOLO_EXHIBITION = '個展',
        C_BOOK = '本',
        D_APP = 'アプリ',
        E_AWARD = '受賞歴など',

    title = models.CharField(max_length=200)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField(blank=True, null=True)
    place = models.CharField(max_length=200, blank=True, null=True)
    link_url = models.URLField(blank=True, null=True)
    genre = models.CharField(
        max_length=5, choices=Genre.choices, default=Genre.A_GROUP_EXHIBITION)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.is_public == False:
            is_public_text = "(非公開)"
        else:
            is_public_text = ""
        return '%s  %s' % (self.title, is_public_text)
