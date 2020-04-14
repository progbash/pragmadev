from django.db import models
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField
from django.utils.text import slugify
from tinymce.models import HTMLField

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_description = HTMLField()
    task_url = models.URLField(max_length=300, blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, editable=False)
    task_source = models.CharField(max_length=50, blank=True, null=True)
    task_deadline = models.DateTimeField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name

    def save(self, *args, **kwargs):
        self.slug = latin_slugify(self.task_name)
        super(Task, self).save(*args, **kwargs)

def latin_slugify(str):
    str = str.replace(" ", "-")
    str = str.replace("?", "-")
    str = str.replace(",", "-")
    str = str.replace("ə", "e")
    str = str.replace("ö", "o")
    str = str.replace("ç", "ch")
    str = str.replace("ş", "sh")
    str = str.replace("ı", "i")
    str = str.replace("ü", "u")
    str = str.replace("ğ", "gh")
    str = str.replace("İ", "i")
    str = str.replace("Ə", "e")
    str = str.replace("Ö", "o")
    str = str.replace("Ü", "u")
    return str.lower()

class TaskFeedback(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    sender = CurrentUserField()
    is_solved = models.BooleanField()
    feedback_content = models.TextField(max_length=1000, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.feedback_content