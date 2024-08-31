from django import forms
from .models import Ticket

# Ticket Form
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['issue_type', 'custom_issue', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe your issue...'}),
        }
