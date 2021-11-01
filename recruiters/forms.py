from django import forms
from .models import Job


class NewJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location',
                  'description', 'skills_req', 'job_type', 'link']
        help_texts = {
            'skills_req': 'Enter all the skills required each separated by commas.',
            'link': 'Link for the next round',
        }


class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location',
                  'description', 'skills_req', 'job_type', 'link']
        help_texts = {
            'skills_req': 'Enter all the skills required each separated by commas.',
            'link': 'Link for the next round',
        }
