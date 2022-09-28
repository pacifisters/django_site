from django.urls import path
from .views import FileDetail

urlpatterns = [
    path('', FileDetail.as_view(), name='index'),

]


