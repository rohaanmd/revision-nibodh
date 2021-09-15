from django.db import models
from django.utils import timezone
# Create your models here.

class blog(models.Model):

    title = models.CharField(max_length=70)
    body =  models.CharField(max_length=700)
    # author = models.ForeignKey()
    author =  models.CharField(max_length=50,default="rohaan")
    pub_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="blog\images",default="https://via.placeholder.com/500x500.png?text=Default")

    def __str__(self):
        return self.title + " | " + self.author

    # class Meta:
    #     managed = True
    #     verbose_name = 'blog'
    #     verbose_name_plural = 'blogs'