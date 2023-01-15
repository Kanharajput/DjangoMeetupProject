from .models import Participants
from django.forms import ModelForm

class RegistrationForm(ModelForm):
    class Meta:
        model = Participants
        fields = "__all__"