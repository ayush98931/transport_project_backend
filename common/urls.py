from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('google_register/' , register_with_google),
    path('google_sign_in/' , sigin_with_google),
    path('manual_sign_in/' , sigin_in_manual),
    path('manual_register/' , register_maual),
    path('logout/' , logout)
]
