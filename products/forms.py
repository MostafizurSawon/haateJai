from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Task, TaskCategory
from django import forms

# class UserTaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['skill_category', 'topics', 'pending_date'] 
        
#         labels = {
#             'skill_category': 'Skill Category',
#             'topics': 'Topics',
#             'pending_date': 'Pending Date and Time',
#         }
    
#     pending_date = forms.DateTimeField(
#         widget=forms.DateTimeInput(attrs={"type": "datetime-local"}), 
#         label="Pending Date and Time"
#     )

        
# class UpdateUserTaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         # fields = '__all__'
#         fields = ['skill_category', 'topics','complete', 'pending_date' ] 
        
#         widgets = {
#             'pending_date': forms.DateInput(attrs={'readonly': 'true'}),
#         }
        
#         labels = {
#             'skill_category': 'Skill Category',
#             'topics': 'Topics',
#             'pending_date': 'Pending date',
#         }
        
        
        
