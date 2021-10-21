from django.urls import path

from .views import BackfillView

urlpatterns = [
    path('', BackfillView.as_view(), name='list')
]
