from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    cat = (
        ("Top Trends", "Top Trends"),
        ("Innovations", "Innovations"),
        ("Entertainment", "Entertainment"),
        ("AI", "AI"),
        ("Innovations", "Innovations"),
        ("Good Reads", "Good Reads"),
        ("Digital Marketing", "Digital Marketing"),
        ("Programming", "Programming"),
        ("Technology", "Technology"),
        ("Business", "Business"),
    )
    BlogID = models.CharField(max_length = 10, default = "")
    BlogName = models.CharField(max_length=100, blank=False, default="")
    BlogDescription = models.CharField(max_length=500, blank=False, default="")
    BlogKeywords = models.CharField(max_length = 5000, blank = False, default = "")
    BlogDateAdded = models.CharField(max_length=20, blank=False, default="")
    BlogImage = models.CharField(max_length = 5000, default = "")
    BlogSlug = models.CharField(max_length=400, default="")
    BlogCategory = models.CharField(max_length=100, choices=cat, default="")
    BlogPost = models.TextField(max_length=10000, blank=False, default="")
    BlogAuthor = models.CharField(max_length=50, blank=False, default="")
    Views = models.CharField(max_length=50, blank=False, default="0")
    Likes = models.ManyToManyField(User, related_name="UserLikes", blank=True)

    def __str__(self) -> str:
        return self.BlogName

class PostComment(models.Model):
    PostID = models.CharField(max_length = 1000, default = "")
    Name = models.CharField(max_length = 100, default = "")
    Email = models.CharField(max_length = 100, default = "")
    Message = models.CharField(max_length = 10000, default = "")
    Date = models.CharField(max_length = 100, default = "")

    def __str__(self) -> str:
        return self.Message

