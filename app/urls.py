from django.urls import path
from app.views import index, add_file, delete_file, download_file, one_object_delete

app_name = "app"

urlpatterns = [
    path('', index, name="index"),
    path('add-file/', add_file, name="add-file"),
    path('delete-file/', delete_file, name="delete-file"),
    path("download/<int:pk>/", download_file, name="download"),
    path("delete/<int:pk>/", one_object_delete, name="one-delete"),
]
