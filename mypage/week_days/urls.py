from django.urls import path
from . import views as views_days

urlpatterns = [
    path('<int:sign_zo>/', views_days.get_int_of_days),
    path('<str:sign_zo>/', views_days.get_day, name='week_name'),
#посмотреть какого хуя name надо ставить в str
]
