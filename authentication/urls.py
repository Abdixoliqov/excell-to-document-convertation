from django.urls import path
from authentication.views import logins, login_page, logout_page

app_name = 'auth'

urlpatterns = [
    path('login/', login_page, name="login"),
    path('logins/', logins, name="logins"),
    path('logout/', logout_page, name="logout")
]