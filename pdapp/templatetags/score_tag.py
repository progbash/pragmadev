from django import template
register = template.Library()

from ..models import Task, TaskFeedback

@register.simple_tag(takes_context=True)
def score_tag(context):
    request = context['request']
    solved_personal = TaskFeedback.objects.filter(is_solved=True).filter(sender_id=request.user.id)
    tasks_count = Task.objects.all().count()
    user_score = int((solved_personal.count()/tasks_count)*10)

    return user_score

@register.simple_tag(takes_context=True)
def solved_tag(context):
    request = context['request']
    solved_personal = TaskFeedback.objects.filter(is_solved=True).filter(sender_id=request.user.id).count()

    return solved_personal

@register.simple_tag(takes_context=True)
def tasks_count(context):
    tasks_count = Task.objects.all().count()

    return tasks_count
