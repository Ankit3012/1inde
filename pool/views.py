from django.shortcuts import render
from .models import Ghadi
import requests
from django.http import JsonResponse
from datetime import date
from django.views import View
# Create your views here.
class GetTableDataView(View):
    def get(self, request, *args, **kwargs):
        data = list(Ghadi.objects.values()[:10])
        return JsonResponse({'data': data})
def index(request):
    if request.method == 'POST':
        month = request.POST.get('month')
        year = request.POST.get('year')
        print(month,year)
        if month and year:

            alldata = Ghadi.objects.filter(
                date__month=int(month),
                date__year=int(year)
            ).order_by('date')

            print('current:--',alldata)
            return render(request, 'index.html', {'alldata': alldata, 'selected_month': month, 'selected_year': year})
    data = list(Ghadi.objects.values()[:10])
    cur_data = Ghadi.objects.values()[:1]
    print(cur_data)

    return render(request,'index.html',{'data': data,'cur_data': cur_data})

def crypto(request):
    key = "https://api.binance.com/api/v3/ticker/price?symbol="
    # Making list for multiple crypto's
    currencies = ["BTCUSDT", "DOGEUSDT", "LTCUSDT"]
    j = 0
    crypto={}
    # running loop to print all crypto prices
    for i in currencies:

        url = key + currencies[j]
        data = requests.get(url)
        data = data.json()
        j = j + 1

        crypto[data['symbol']] = data['price']
    print(crypto)
    return render(request,'crypto.html',{'crypto':crypto})
def get_crypto_data(request):
    key = "https://api.binance.com/api/v3/ticker/price?symbol="

    # Making list for multiple crypto's
    currencies = ["BTCUSDT", "DOGEUSDT", "LTCUSDT"]
    crypto = {}

    # Running loop to get all crypto prices
    for currency in currencies:
        url = key + currency
        data = requests.get(url).json()
        crypto[data['symbol']] = data['price']

    return JsonResponse(crypto)
def charts(request):
    if request.method == 'POST':
        month = request.POST.get('month')
        year = request.POST.get('year')
        # print(month, year)
        if month and year:
            # Assuming that the 'month' and 'year' fields in the Ghadi model are integers
            # You may need to adjust the field types and filtering logic based on your actual model

            alldata = Ghadi.objects.filter(
                date__month=int(month),
                date__year=int(year)
            ).order_by('-date')

            # print('current:--', alldata)
            return render(request, 'charts.html', {'alldata': alldata, 'selected_month': month, 'selected_year': year})
    current_date = date.today()
    alldata = Ghadi.objects.filter(
        date__month=current_date.month,
        date__year=current_date.year
    ).order_by('-date')
    # print(alldata)
    return render(request, 'charts.html', {'alldata': alldata})
def info(request):
    return render(request,'info.html')
