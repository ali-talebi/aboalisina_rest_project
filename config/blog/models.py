from django.db import models

# Create your models here.


class Post_Category(models.Model):
    post_category_name = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.post_category_name}'
    
    class Meta:
        db_table = "post_category_table"
        verbose_name_plural = "post category management"



class Post(models.Model):
    
    post_banner_picture = models.FileField(upload_to="blog_post_picture/")
    alternative_banner_picture = models.CharField(max_length=30)
    video_banner = models.FileField(upload_to="blog_post_video/",null=True,blank=True)
    post_name = models.CharField(max_length=100)
    post_text = models.TextField()
    category  = models.ForeignKey(Post_Category,on_delete=models.SET_NULL,blank=True,null=True,related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.post_name}'
    
    class Meta:
        db_table = "post_table"
        verbose_name_plural = "post management"