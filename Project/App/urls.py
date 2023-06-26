from django.urls import path
from .views import *

urlpatterns = [
    
    # path ('login/',login, name='login'),
    
    path ('employee_registration/',employee_registration, name='registration'),
    
    path('success/', success, name='success'),
    
]
