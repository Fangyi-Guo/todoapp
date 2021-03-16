from django.db import models
from datetime import datetime

# Create your models here.
class StickyNote(models.Model):
    note_name = models.CharField(max_length=100)
    def __str__(self):
        return self.note_name

class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    note = models.ForeignKey(StickyNote, default=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


