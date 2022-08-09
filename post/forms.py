
from django import forms
from .models import Profile


# creating a form
class ProfileForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Profile

        # specify fields to be used
        fields = [
            "bio",
            "capa",
            ]
