from django.db import models

from django.db import models
from datetime import date
from django.template.defaultfilters import slugify
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
# Create your models here.

"""
 # blog/models module defines the schema for the generated database tables.
 # Each class defines a table structure with each defined attribute
 # representing the given columns for the table.  Defined methods allow for
 # controllers of the data upon update/creation/deletion of entries.
 # 
 # These models represent the necessary components for the blog app of the web-platform
 #
 # @author Andrew Burton
 # @version 1.0
 # @since 1.0
 # @see /*insert app directory path*/
"""


"""
Add model docs here
"""


class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


"""
Add model docs here
"""


class Post(models.Model):
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )
    title = models.CharField(max_length=250)
    image = models.ImageField()
    body = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    activities = GenericRelation('Activity')
    slug = models.SlugField(max_length=200, unique_for_date='Publish')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, default='Draft', choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Activity(models.Model):
    ACTIVITY_CHOICES = (
        ('F', 'Favorite'),
        ('L', 'Like'),
        ('U', 'Up Vote'),
        ('D', 'Down Vote')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.ForeignKey(to='Comment', related_name='commments', on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    activities = GenericRelation(Activity)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return self.body


class Tutorial(models.Model):
    title = models.CharField(max_length=250)
    posts = models.ManyToManyField('Post', through='TutorialPost')


class TutorialPost(models.Model):
    tutorial = models.ForeignKey('Tutorial', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    position = models.IntegerField()

    class Meta:
        ordering = ['position']
