from django.urls import include, path
from .views import AdminRegistrationView


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/registration/admin', AdminRegistrationView.as_view(), name='employee-reg'),
    path('account/', include('allauth.urls')),
]
