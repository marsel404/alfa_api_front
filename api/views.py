from email import contentmanager
from locale import currency
from rest_framework.response import Response
from api.models import CurrencyPairs
from rest_framework.views import APIView
import sqlite3
from django.shortcuts import render


class MinMaxAPIView(APIView):
    def get(self, request, cur_pair, day_yesterday, day_tommorow):
        currency_pair = CurrencyPairs.objects.filter(
            currency_pair=cur_pair).values()
        id = currency_pair[0].get('id')

        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()

        min = cursor.execute(
            "SELECT * FROM api_currencypair WHERE currency_pair_id == ? AND date BETWEEN ? AND ? ORDER BY min",
            (id, day_yesterday, day_tommorow)).fetchone()
        max = cursor.execute(
            "SELECT * FROM api_currencypair WHERE currency_pair_id == ? AND date BETWEEN ? AND ? ORDER BY -max",
            (id, day_yesterday, day_tommorow)).fetchone()
        return Response({'Валютная пара': cur_pair, 'Начало периода': day_yesterday,
                        'Окончание периода': day_tommorow, 'Минимальная цена': min[2], 'Максимальная цена': max[3]})


class ListAPIView(APIView):
    def get(self, request, cur_pair, day_yesterday, day_tommorow):
        currency_pair = CurrencyPairs.objects.filter(
            currency_pair=cur_pair).values()
        id = currency_pair[0].get('id')

        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        data = cursor.execute("SELECT * FROM api_currencypair WHERE currency_pair_id == ? AND date BETWEEN ? AND ?",
                              (id, day_yesterday, day_tommorow)).fetchall()
        return Response({'Валютная пара': cur_pair, 'Начало периода': day_yesterday,
                        'Окончание периода': day_tommorow, 'Дата, мин. цена, макс. цена': list(data)})


def index(request):
    currency_pairs = CurrencyPairs.objects.all()
    context = {'currency_pairs': currency_pairs}
    return render(request, 'api/index.html', context)


def minmax(request, value):
    currency_pair = CurrencyPairs.objects.filter(id=value).values()
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    min = cursor.execute(
        "SELECT * FROM api_currencypair WHERE currency_pair_id == ? ORDER BY min",
        (value, )).fetchone()
    max = cursor.execute(
        "SELECT * FROM api_currencypair WHERE currency_pair_id == ? ORDER BY -max",
        (value, )).fetchone()

    context = {'currency_pair': currency_pair[0].get(
        'currency_pair'), 'min': min[2], 'max': max[3]}
    return render(request, 'api/minmax.html', context)


def list(request, value):
    currency_pair = CurrencyPairs.objects.filter(id=value).values()
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    data = cursor.execute("SELECT * FROM api_currencypair WHERE currency_pair_id == ? ORDER BY -id",
                          (value, )).fetchmany(10)
    context = {'currency_pair': currency_pair[0].get(
        'currency_pair'), 'data': data}
    return render(request, 'api/list.html', context)
