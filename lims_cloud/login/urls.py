from django.conf.urls import url
from views import LoginView , CreateUser



urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^add_user/$', CreateUser.as_view(), name='add_user'),
]

