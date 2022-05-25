from django.urls import path
from .views import *
from . import views
from .models import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('tax', TaxView.as_view(), name='tax'),
    path('analytics', views.analytics, name='analytics'),
]
