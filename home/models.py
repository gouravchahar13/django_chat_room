from django.db import models

# Create your models here.


class chatroom(models.Model):
    username=models.CharField(max_length=150,null=True)
    content=models.CharField( max_length=150)
    image=models.ImageField( upload_to='./static/images', height_field=None, width_field=None, max_length=None,blank=None)
    file=models.FileField( upload_to='./files/', max_length=100,blank=None)
    timestamp=models.DateTimeField(auto_now=True,null=True)
    