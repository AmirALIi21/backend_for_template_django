from django.db import models
#my models.py
class Creator (models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(max_length=100)
    is_active = models.BooleanField(default=True)

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

class Project(models.Model):
    title = models.CharField(max_length=200)
    CATEGORY_CHOICES=(
        ('all','All'),
        ('photography','Photography'),
        ('logo','Logo'),
        ('graphics','Graphics'),
        ('advertising','Advertising'),
        ('fashion','Fashion'),
    )
    category = models.CharField(choices =CATEGORY_CHOICES,default='all' ,max_length=20)
    image = models.ImageField(upload_to='tsk1/static/tsk1/img/portfolio/', blank=True , null=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    

class SocialLink(models.Model):
    platform = models.CharField(max_length=200)
    link = models.URLField()

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='tsk1/static/tsk1/', blank=True , null=True)
    is_active = models.BooleanField(default=True)
