from django.urls import path

from message.views import HomeView, Success, GetCredentialInfoView

urlpatterns = [
    path('api/credentials/', GetCredentialInfoView.as_view()),
    path('', HomeView.as_view(), name='home'),
    path('success/', Success.as_view())
    ]