from django.contrib.auth.models import User, auth
from django.db import models

# Create your models here.
class Tag(models.Model): # Tag of a post, will be generated by admin only
    name = models.CharField(max_length=50)
    adminOnly = models.BooleanField(default=False)

class Post(models.Model): # Post 
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    post_Type = models.CharField(max_length=50, default='forum')

class Comment(models.Model): # Comment of a post
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    likes = models.IntegerField(default=0)

class Like(models.Model): # Post/comment like
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)

# class Message(models.Model): # The message of the chat
#     id = models.AutoField(primary_key=True)
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     read = models.BooleanField(default=False)

# class Chat(models.Model): # Chat to who ..
#     id = models.AutoField(primary_key=True)
#     users = models.ManyToManyField(User)
#     messages = models.ManyToManyField(Message)

class TestHistory(models.Model): # Test history
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.TextField()
    quiz_type = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # The user who is notified
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True) # Notification in post, ex: someone commented ...
    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True) # Notifcation in comment, ex: someone replied
    # message = models.ForeignKey(Message, on_delete=models.CASCADE, null=True) # Notifcation in message, ex: a message received from ...
    notification_Content = models.TextField(max_length=500) # The notification message, will be auto generated based on the notification type
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    # cek post apa aja, if post.user.id == user.id
    # cek notif, if notif.user.id == user.id

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='reporter') # The one that reports
    reportedUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='reported') # If reporting a user
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True) # If reporting a post
    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True) # If reporting a comment
    reason = models.CharField(max_length=200)
    reportType = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)