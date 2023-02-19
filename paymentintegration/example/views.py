from django.shortcuts import render
import requests
import json 
from django.http import JsonResponse, HttpResponseRedirect
from .models import *

# Create your views here.
def checkoutpage(request):
    return render(request, 'payment.html')
def payment(request):
    data = {
        "return_url": "http://127.0.0.1:8000/verify",
        "website_url": "http://127.0.0.1:8000/",
        "amount": 1500,
        "purchase_order_id": "test12",
        "purchase_order_name": "test",
        "customer_info": {
        "name": "Ashim Upadhaya",
        "email": "example@gmail.com",
        "phone": "9811496763"
        },
        "amount_breakdown": [
        {
                "label": "Mark Price",
                "amount": 1000
        },
        {
                "label": "VAT",
                "amount": 150
        },
        {
                "label": "Service charge",
                "amount": 100
        },
        {
                "label": "Due",
                "amount": 50
        },
        {
                "label": "After dues",
                "amount": 200
        }
        ],
        "product_details": [
        {
                "identity": "1234567890",
                "name": "Khalti logo",
                "total_price": 100,
                "quantity": 1,
        "unit_price": 1300
        }
        ]


    }
    headers = {
            "Authorization": "Key 3f4159b5f85840fdab55ce0670f53e6d"  

    }
    response = requests.post("https://a.khalti.com/api/v2/epayment/initiate/", json=data, headers=headers)
    print(response, response.text)
    if response.status_code == 200:
        data = response.json()
        pidx = data.get("pidx")
        
        payment = verification(pidx=pidx)
        payment.save()
        return HttpResponseRedirect(data.get("payment_url"))
        


def verify(request):
    payment = verification.objects.last()
    pidx = payment.pidx
    data = {
        "pidx": pidx
    }
    headers = {
        "Authorization": "Key 3f4159b5f85840fdab55ce0670f53e6d"  
    }
    response = requests.post("https://a.khalti.com/api/v2/epayment/lookup/", json=data, headers=headers)
    data = response.json()
    status = data.get("status")
    pidx = data.get("pidx")

    status = payment_status(status=status)
    status.save()
    pidx = payment_status(pidx=pidx)

    return JsonResponse(data)






