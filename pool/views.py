from django.shortcuts import render,redirect
from .models import Ghadi
import requests
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from datetime import date
from django.views.decorators.csrf import csrf_exempt
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
@csrf_exempt
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
@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
def login(request):
    if request.method == 'POST':
        # if request.POST.get('email'):
        email=request.POST.get('email')
        password=request.POST.get('pass')
        if email=='ag61219130' and password=='python@123':
            return redirect('edit_all_ghadi')
        else:
            return render(request, 'login.html')

    return render(request,'login.html')

@csrf_exempt
def edit_all_ghadi(request):

    ghadi_data = Ghadi.objects.all()[:10]

    if request.method == 'POST':
        for ghadi in ghadi_data:
            ghadi.sn = request.POST.get(f'sn_{ghadi.id}')
            ghadi.fb = request.POST.get(f'fb_{ghadi.id}')
            ghadi.gb = request.POST.get(f'gb_{ghadi.id}')
            ghadi.nazi = request.POST.get(f'nazi_{ghadi.id}')
            ghadi.dl = request.POST.get(f'dl_{ghadi.id}')
            ghadi.date = request.POST.get(f'date_{ghadi.id}')
            ghadi.save()

        return render(request,'diclare.html')

    context = {
        'ghadi_data': ghadi_data,
    }

    return render(request,'diclare.html',context)

@csrf_exempt
def create_default_data(request):
    # Create new default data
    Ghadi.objects.create()

    return redirect('edit_all_ghadi')


def delete_ghadi_record(request, pk):
    ghadi = get_object_or_404(Ghadi, pk=pk)

    if request.method == 'DELETE':
        ghadi.delete()
        return JsonResponse({'message': 'Record deleted successfully.'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)