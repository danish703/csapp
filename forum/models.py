from django.db import models

# Create your models here.
class Post(models.Model):
    post_image_url = models.ImageField(blank=True,null=True)
    post_status = models.TextField()
    posted_by_userId = models.CharField(max_length=255)
    posted_by_semester = models.CharField(max_length=15)
    posted_by_userImage = models.CharField(verbose_name="Image url",null=True,blank=True,max_length=255)
    posted_by_username = models.CharField(max_length=255)
    device_id = models.CharField(max_length=255,default=1)

    def __str__(self):
        return self.posted_by_username

class Comments(models.Model):
    comment = models.TextField()
    comment_user_id = models.CharField(max_length=255)
    comment_user_photo = models.CharField(verbose_name="Image url",blank=True,null=True,max_length=255)
    comment_username = models.CharField(verbose_name="username",max_length=255)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment