from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Task, TaskFeedback
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class TaskAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

class TaskFeedbackAdmin(admin.ModelAdmin):
    list_display = ['task', 'sender', 'is_solved', 'feedback_content', 'date_added']

admin.site.site_header = "Pragmadev - Admin Dashboard" 
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskFeedback, TaskFeedbackAdmin)
admin.site.unregister(Group)