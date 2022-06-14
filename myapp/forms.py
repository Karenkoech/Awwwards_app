from django import forms
from .models import Project, Rating
 

class ProjectUploadForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ["title","description","link","image"]

class RatingUploadForm(forms.ModelForm):
    
    class Meta:
        model = Rating
        fields = ["design","usability","content"]