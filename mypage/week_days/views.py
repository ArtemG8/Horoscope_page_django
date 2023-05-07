from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

days_of_week = {
    "Понедельник": "Первый день рабочей недели",
    "Вторник": "Второй день рабочей недели",
    "Среда": "Третий день рабочей недели",
    "Четверг": "Четвертый день рабочей недели",
    "Пятница": "Пятый день рабочей недели",
    "Суббота": "Первый выходной день",
    "Воскресенье": "Второй выходной день"
}


# Create your views here.
def get_day(request, sign_zo: str):
    description = days_of_week.get(sign_zo)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'{sign_zo} - такая команда не найдена :(')


def get_int_of_days(request, sign_zo: int):
    days = list(days_of_week)
    if sign_zo > len(days):
        return HttpResponseNotFound('Такого знака нет :(')
    else:
        name_days = days[sign_zo - 1]
        url_redirect = reverse('week_name', args=(name_days,))
        return HttpResponseRedirect(url_redirect)
