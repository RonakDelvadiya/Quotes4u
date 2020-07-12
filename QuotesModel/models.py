from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils import timezone

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
       Token.objects.create(user=instance)

# Day
class Days(models.Model):
    dayname = models.CharField("Day",max_length=100,unique=True,default="")
    dateofday = models.DateField(null=True,blank=True)
    dayhistory = models.TextField("History",default="",null=True)
    created_at = models.DateTimeField(auto_now_add=True,default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
		verbose_name = "Day"
		verbose_name_plural = "Day"

    def __str__(self):
	    return self.dayname

# Ocuupation
class Occupation(models.Model):
    occupation = models.CharField("Ocuupation",max_length=100,unique=True)    
    created_at = models.DateTimeField(auto_now_add=True,default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
		verbose_name = "Occupation"
		verbose_name_plural = "Occupation"

    def __str__(self):
	    return self.occupation
    
# Author
class Author(models.Model):
    name = models.CharField("Author's Name",max_length=100,unique=True)
    occupationid = models.ForeignKey(Occupation,null=True,blank=True)    
    created_at = models.DateTimeField(auto_now_add=True,default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
		verbose_name = "Author"
		verbose_name_plural = "Author"

    def __str__(self):
	    return self.name

# category
class Category(models.Model):
    category = models.CharField("Category",max_length=100,unique=True,blank=False,null=False)    
    created_at = models.DateTimeField(auto_now_add=True,default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Category"

    def __str__(self):
	    return self.category

# Quotes
class Quotes(models.Model):
    quotesday = models.ForeignKey(Days,null=True,blank=True)
    authorid = models.ForeignKey(Author,verbose_name="Select Auther",)
    quote = models.CharField("Quote",max_length=255,unique=True)
    category = models.ManyToManyField(Category,verbose_name="Select Category",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
		verbose_name = "Quotes"
		verbose_name_plural = "Quotes"

    def get_category(obj):
        return "\n  ".join([p.category for p in obj.category.all()])

    def __str__(self):
	    return self.quote