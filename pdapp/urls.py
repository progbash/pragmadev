from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('task_details', views.task_details, name='task_details'),
    path('task_details/<slug:slug>', views.task_details, name='task_details'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('instruction', views.instructions, name='instructions')
]