from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'title',
            'company',
            'location',
            'education',
            'experience',
            'job_type',
            'package',
            'description',
            'apply_url',
            'company_logo',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
