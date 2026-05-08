from django.db import models

# Create your models here.

class School_Comments(models.Model):
    commenter_picture = models.FileField(null=True,blank=True,upload_to="school_commenter_picture/")
    commenter_name = models.CharField(max_length=50)
    commenter_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.commenter_name}'
    
    class Meta:
        db_table = "school_comments_table"
        verbose_name_plural = "school comments management"