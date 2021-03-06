from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ad(models.Model):
    code = models.CharField(max_length=12,blank=True, null=True)
    owner = models.ForeignKey(User,related_name='ad_owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField( upload_to='ad/')
    content = models.TextField(max_length=1000)
    price = models.IntegerField(default=1)
    category = models.ForeignKey('Category',limit_choices_to={'main_category':True},related_name='ad_category', on_delete=models.CASCADE)

    ### relation : main category 

    def save(self, *args, **kwargs): 
        ## logic
        self.code = '##'+((str(self.id)).center(10,'0'))
        super(Ad, self).save(*args, **kwargs) 


    def __str__(self):
        return self.name





class AdImages(models.Model):
    ad = models.ForeignKey(Ad, related_name='ad_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ad_images/')



class Category(models.Model):
    name = models.CharField(max_length=50)
    main_category = models.ForeignKey('self', limit_choices_to={'main_category':None},related_name='maincategory', on_delete=models.CASCADE , blank=True, null=True)

    ## relation sub category 

    def __str__(self):
        return self.name