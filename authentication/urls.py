from django.conf.urls import url

from .views import RegistrationAPIView, LoginAPIView, UserListViewSet

urlpatterns = [
    url(r'^users?$', UserListViewSet.as_view({'get': 'list'}), name='user_list'),
    url(r'^users/register?$', RegistrationAPIView.as_view(), name='register'),
    url(r'^users/login?$',LoginAPIView.as_view(), name='login'),
]