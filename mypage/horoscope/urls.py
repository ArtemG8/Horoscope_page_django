from django.urls import path
from . import views as views_horo
from week_days import views as views_days

urlpatterns = [
    path('horoscope/type/', views_horo.get_type),

    # path('<int:sign_zodiac>/', views_horo.get_info_number),
    path('<str:sign_zodiac>/', views_horo.get_info_word, name='horoscope_name'),

# path('<int:sign_zodiac>/', views_horo.get_info_number),
]
