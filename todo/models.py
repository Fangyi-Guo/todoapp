from django.db import models
from datetime import datetime

from django.dispatch import receiver
from django.db.models.signals import (
    pre_save,
    post_save
)

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

#auto create some field before the instance is created
@receiver(pre_save,sender=StickyNote)
def stickynote_pre_save_handler(sender, instance, *args, **kwargs):
    """
    before saved in the database
    """
    print(instance.note_name,instance.id) # might be None

#notify after the instance is created
@receiver(post_save,sender=StickyNote)
def stickynote_created_handler(sender, instance, created, *args, **kwargs):
    """
    after saved in the database
    """
    if created:
        print("Send email to",  instance.note_name)
    else:
        print(instance.username, "was just saved")

#post_save.connect(stickynote_created_handler, sender=Todo)
#trigger presave
#instance.save()
#trigger postsave