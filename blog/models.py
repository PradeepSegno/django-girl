from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager
# from django.contrib.auth.admin import UserAdmin

import os


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody'))


class User(AbstractUser):
    mobile = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=CHOICES, default='Male')
    dob = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='user/', blank=True, null=True)
    role = models.CharField(max_length=55)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "01. Users"


# ############### Category model starts here ###############


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    auther = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)


# ############### Post model starts here ###############


class Post(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True)
    slug = models.SlugField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    tags = TaggableManager()
    # tags = models.ManyToManyField(
    #     Tag, default='tag', max_length=100, choices=Category_choices)
    # category = models.ForeignKey(
    #     Category, on_delete=models.CASCADE, default=1)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # tags = models.ManyToManyField(Tag)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


# ############### Comment model starts here ###############


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


# ############### Profile model starts here ###############


# class Profile(models.Model):
#     user = models.OneToOneField(
#         User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pic')
#     gender = models.CharField(
#         max_length=1, choices=CHOICES, blank=True, null=True)

#     def __str__(self):
#         return f'{self.user.username} Profile'


# class UserAdmin(BaseUserManager):
#     def create_user(self, email, password=None):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email=self.normalize_email(email),
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_staffuser(self, email, password):
#         """
#         Creates and saves a staff user with the given email and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.staff = True
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.staff = True
#         user.admin = True
#         user.save(using=self._db)
#         return user

# hook in the New Manager to our Model
