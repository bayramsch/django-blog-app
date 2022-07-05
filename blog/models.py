from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    status_CHOICES = [
        ('p','Published'),
        ('d','Draft')
        ]
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=250)
    logo_img = models.ImageField(upload_to='images', blank=True, null=True, default="images/programing.png")
    category = models.ForeignKey(Category,on_delete=models.PROTECT, default=1)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=status_CHOICES)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title
    
    def comment_count(self):
        return self.comment_set.all().count()
    
    def like_count(self):
        return self.like_set.all().count()
    
    def view_count(self):
        return self.viewpost_set.all().count()
    
    def comments(self):
        return self.comment_set.all()
        
    
    # print(view_count)
    
        
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=200)
    
    def __str__(self):
        return self.user.username

    

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

    
class ViewPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username