from .forms import CreateUserForm, CreateFeedbackForm
from .models import Task, TaskFeedback
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def index(request):
    tasks = Task.objects.all().order_by('-id')
    context = {
        'tasks': tasks,
    }
    return render(request, 'index.html', context)

@login_required(login_url='sign_in')
def task_details(request, slug):
    if slug:
        task = get_object_or_404(Task, slug=slug)
        today = datetime.now().date()
        deadline = task.task_deadline.date()
        time_left = deadline - today
        form = CreateFeedbackForm()
        feedback = TaskFeedback.objects.filter(task_id=task.id)
        solved_general = feedback.filter(is_solved=True)
        solved_or_not =  solved_general.filter(sender_id=request.user.id)
        did_submit = feedback.filter(sender_id=request.user.id)
        # Getting user score
        solved_personal = TaskFeedback.objects.filter(is_solved=True).filter(sender_id=request.user.id)
        tasks_count = Task.objects.all().count()
        user_score = int((solved_personal.count()/tasks_count)*10)
        

    if request.method == 'POST':
        messages.info(request, 'Feedback göndərildi.')
        form = CreateFeedbackForm(request.POST)
        if form.is_valid():
            new_feedback = form.save(commit=False)
            new_feedback.task = task
            new_feedback.save()
            return redirect('index')
    else:
        form = CreateFeedbackForm(request.POST)
        
    context = {
        'task': task,
        'form': form,
        'days_left': time_left.days,
        'feedback': feedback,
        'solved_general': solved_general,
        'solved_personal': solved_personal,
        'tasks_count': tasks_count,
        'user_score': user_score,
        'solved_or_not': solved_or_not,
        'did_submit': did_submit
    }
    return render(request, 'task-details.html', context)

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            user_name = request.POST.get('first_name')
            user_email = request.POST.get('email')
            subject = 'PragmaDevə xoş qoşuldun !'
            message = 'Salam, ' + str(user_name) + '. \nKod yazan barmaqların dərd görməsin.'
            from_email = settings.SERVER_EMAIL
            recipient_list = [user_email]
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, 'PragmaDev hesabın yaradıldı.')
            if form.is_valid():
                form.save()
                return redirect('sign_in')
        context = {'form': form}
        return render(request, "sign_up.html", context)

def sign_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(
                    request, 'İstifadəçi adı və ya parol yanlışdır.')

        context = {}
        return render(request, "sign_in.html", context)

def sign_out(request):
    logout(request)
    return redirect('/')

def instructions(request):
    return render(request, 'instructions.html', {})