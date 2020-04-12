from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TaskFeedback
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

    # first_name
        self.fields['first_name'].widget.attrs['id'] = 'first_name'
        self.fields['first_name'].widget.attrs['class'] = 'input--style-3'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Ad'
        self.fields['first_name'].widget.attrs['autocomplete'] = 'off'
        self.fields['first_name'].widget.attrs['required'] = 'required'
        self.fields['first_name'].widget.attrs['type'] = 'text'
        self.fields['first_name'].widget.attrs['name'] = 'first_name'

    # last_name
        self.fields['last_name'].widget.attrs['id'] = 'last_name'
        self.fields['last_name'].widget.attrs['class'] = 'input--style-3'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Soyad'
        self.fields['last_name'].widget.attrs['autocomplete'] = 'off'
        self.fields['last_name'].widget.attrs['required'] = 'required'
        self.fields['last_name'].widget.attrs['type'] = 'text'
        self.fields['last_name'].widget.attrs['name'] = 'last_name'

    # email
        self.fields['email'].widget.attrs['id'] = 'email'
        self.fields['email'].widget.attrs['class'] = 'input--style-3'
        self.fields['email'].widget.attrs['placeholder'] = 'Elektron Poçt'
        self.fields['email'].widget.attrs['autocomplete'] = 'off'
        self.fields['email'].widget.attrs['required'] = 'required'
        self.fields['email'].widget.attrs['type'] = 'email'
        self.fields['email'].widget.attrs['name'] = 'email'

    # username
        self.fields['username'].widget.attrs['id'] = 'username'
        self.fields['username'].widget.attrs['class'] = 'input--style-3'
        self.fields['username'].widget.attrs['placeholder'] = 'İstifadəçi Adı'
        self.fields['username'].widget.attrs['autocomplete'] = 'off'
        self.fields['username'].widget.attrs['required'] = 'required'
        self.fields['username'].widget.attrs['type'] = 'username'
        self.fields['username'].widget.attrs['name'] = 'username'

    # password
        self.fields['password1'].widget.attrs['id'] = 'password1'
        self.fields['password1'].widget.attrs['class'] = 'input--style-3'
        self.fields['password1'].widget.attrs['placeholder'] = 'İstifadəçi Parolu'
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password1'].widget.attrs['required'] = 'required'
        self.fields['password1'].widget.attrs['name'] = 'password1'

    # confirm password
        self.fields['password2'].widget.attrs['id'] = 'password2'
        self.fields['password2'].widget.attrs['class'] = 'input--style-3'
        self.fields['password2'].widget.attrs['placeholder'] = 'Parolu Təkrar Et'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['required'] = 'required'
        self.fields['password2'].widget.attrs['name'] = 'password2'

class CreateFeedbackForm(forms.ModelForm):
    class Meta:
        model = TaskFeedback
        fields = ['feedback_content', 'is_solved']

    def __init__(self, *args, **kwargs):
        super(CreateFeedbackForm, self).__init__(*args, **kwargs)

        self.fields['feedback_content'].widget.attrs['placeholder'] = 'Məsələni həll edərkən qarşılaşdığın sıxıntını, anlaşılmayan hissəni və ya maraqlı qalan məqamları qeyd et.'
        self.fields['feedback_content'].widget.attrs['class'] = 'task-feedback'

    