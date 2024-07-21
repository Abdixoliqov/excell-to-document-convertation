from django import forms
from app.models import FileUpload

class FileForm(forms.Form):  
    class Meta:
        model = FileUpload
        fields = ["excel_file"]