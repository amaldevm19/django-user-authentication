from django.urls import path
from .views import home, signup, login, reset_password, activate_mail

urlpatterns = [
    path('', home, name='home'),
    path('register/', signup, name='signup'),
    path('login/', login, name='login'),
    path('reset-password/', reset_password, name='reset_password'),
    path('activate/<uidb64>/<token>', activate_mail, name="activate"),
]