from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft' 
        PUBLISHED = 'PB', 'Published'
        
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE,
                               realted_name='blue_posts') # way to find who is the author of the post
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now) # date kailan ginawa ang blog
    created = models.DateTimeField(auto_now_add=True) #date kung kailan gumawa or naglagay ng value sa blog
    update = models.DateTimeField(auto_now=True) #update kapag magkakaroon ng bagong value
    
    status = models.CharField(max_length=2,
                              choices=Status,choices,
                              default=Status.DRAFT) #PIPILI LANG 
    
    class Meta:
        ordering = ['-publish'] #bawas if (-) sign ang nasa harap
        index = [
            model.Index(fields=['-publish']):
        ] #para mapabilis ang index ng database, publish ang gagawing index ng code
        #index ay maglalaman ng drafts of post, pwdeng i check before publishing
    
    def __str__(self):
        return self.title