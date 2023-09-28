
from django.forms import ModelForm, PasswordInput
from .models import EmbeddedDashboard

class EmbeddedDashboardForm(ModelForm):
    class Meta:
        model = EmbeddedDashboard
        fields = '__all__'
        widgets = {
            'password': PasswordInput(),
        }