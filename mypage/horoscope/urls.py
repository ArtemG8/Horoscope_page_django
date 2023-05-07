from django.urls import path
from . import views as views_horo

urlpatterns = [
    path('horoscope/type/', views_horo.get_type),
    path('<str:sign_zodiac>/', views_horo.get_info_word, name='horoscope_name'),
]
