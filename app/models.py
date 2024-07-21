from django.db import models
from app.utils import file_path
from django.core.exceptions import ValidationError

def validate_excel(value):
    if not str(value.name).endswith(".xlsx"):
        raise ValidationError(message="Excel file kirita olasiz")
    
class FileUpload(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    excel_file = models.FileField(upload_to=file_path, validators=[validate_excel])
    created = models.DateTimeField(auto_now_add=True)

    def clean(self) -> None:
        print(str(self.excel_file.name).endswith(".xlsx"))
        if not str(self.excel_file.name).endswith(".xlsx"):
            raise ValidationError(message="Excel file kirita olasiz")
    
    def save(self, *args, **kwargs):
        index = str(self.excel_file.name).find(".xlsx")
        name = self.excel_file.name[:index]
        self.name = name
        super(FileUpload, self).save()

    def __str__(self):
        return self.name
