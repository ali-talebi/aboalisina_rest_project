from django.db import models

# Create your models here.



class Banner_Slider(models.Model):
    
    banner_name = models.CharField(max_length=200)
    picture = models.FileField(upload_to="banner_picture_slider/",null=True,blank=True)
    video   = models.FileField(upload_to="banner_video_slider/",null=True,blank=True)
    alternative_text = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    banner_time = models.IntegerField(default=30)
    above_text_banner = models.CharField(max_length=200,null=True,blank=True)
    origin_text_banner = models.CharField(max_length=200,null=True,blank=True)
    warning_text_banner = models.CharField(max_length=200,null=True,blank=True)
    
    
    def __str__(self):
        return f'{self.banner_name}'
    
    class Meta:
        db_table = "banner_slider"
        verbose_name_plural = "banner management part"
    
    
    
    