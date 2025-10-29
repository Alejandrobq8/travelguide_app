from django.shortcuts import render
import requests



def index(request):
    url = "https://v6.exchangerate-api.com/v6/5fc88446d1a8acabe4537209/pair/USD/CRC"
    response = requests.get(url)
    dolares_a_colones = response.json()['conversion_rate']
    amount = 100
    conversion_result = None
    if request.method == "POST":
        try:
            amount = float(request.POST.get("amount", 100))
        except (TypeError, ValueError):
            amount = 100
        conversion_result = round(amount * dolares_a_colones, 2)
    return render(request, "converter/index.html", {
        "conversion_result": conversion_result,
        "amount": amount
    })


