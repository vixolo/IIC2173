import datetime

from django.db import models

class Comment(models.Model):
    comment_text = models.CharField(max_length=500)
    time_sent = models.DateTimeField('date published')
    sender_ip = models.CharField(max_length=100)

    def __str__(self):
        return "Q: " + self.comment_text
