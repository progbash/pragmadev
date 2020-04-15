from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Task, TaskFeedback

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_name', 'task_source', 'task_deadline', 'uploaded_by']

class TaskFeedbackAdmin(admin.ModelAdmin):
    list_display = ['task', 'sender', 'is_solved', 'feedback_content', 'date_added']

class CustomUserAdmin(admin.ModelAdmin):
     list_display = ['first_name', 'last_name', 'last_login']

admin.site.site_header = "Pragmadev - Admin Dashboard" 
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskFeedback, TaskFeedbackAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)