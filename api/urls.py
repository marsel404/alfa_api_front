from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/v1/minmax/<str:cur_pair>/<str:day_yesterday>/<str:day_tommorow>/',
         views.MinMaxAPIView.as_view()),
    path('api/v1/list/<str:cur_pair>/<str:day_yesterday>/<str:day_tommorow>/',
         views.ListAPIView.as_view()),
    path('minmax/<int:value>/', views.minmax, name='minmax'),
    path('list/<int:value>/', views.list, name='list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
