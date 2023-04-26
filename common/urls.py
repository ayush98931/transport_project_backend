from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('google_register/' , register_with_google),
    path('google_sign_in/' , sigin_with_google),

]
