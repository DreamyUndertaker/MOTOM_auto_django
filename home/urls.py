from django.urls import path

from home import views
from home.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='index')
]