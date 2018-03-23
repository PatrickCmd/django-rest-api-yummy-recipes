from django.conf.urls import url

from .views import RegistrationAPIView

urlpatterns = [
    url(r'^users/register?$', RegistrationAPIView.as_view(), name='register')
]