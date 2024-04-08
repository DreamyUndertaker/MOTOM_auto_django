from django.urls import path, include

from home import views
from home.views import HomePageView
app_name = 'home'
urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('shop/', include('db.urls'))
]