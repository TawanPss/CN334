from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

# Create your views here.
def ecommerce_index_view(request) :
    '''This function render index page of ecommerce view'''

    return HttpResponse(" Welcome to 6410742131 Tawan Phonsapsin views!")

def item_view(request, item_id) :
    context_data = {
        "item_id": item_id
    }

    return render(request, 'index.html',context = context_data)

@csrf_exempt
def basic_request(request):
    if request.method == "GET":
        return JsonResponse({"status" : "GET Pass"}, safe=False)
    
    if request.method == "POST":
        return JsonResponse({"status" : "POST Pass"}, safe=False)

@csrf_exempt
def tokenize(request):
    if request.method == "POST":
        try:
            sentence = request.POST['text']
        except:
            return JsonResponse({"error":"Input not found"}, safe=False, status=500)
        url = "https://api.aiforthai.in.th/tlexplus"
        data = {'text':sentence}
        headers = {
            'Apikey': "o5w87jBvYh7PiLfDbmKDtEoEb7DX7hqu"
            }
 
        response = requests.post(url, data=data, headers=headers)
        response_json = response.json()
        return JsonResponse({"student":"student_id", "tokenize":response_json}, safe=False)
    return JsonResponse({"error":"Method not allowed!"}, safe=False, status=403)

@csrf_exempt
def sentimental(request):
    if request.method == "POST":
        try:
            sentence = request.POST['text']
        except:
            return JsonResponse({"error":"Input not found"}, safe=False, status=500)
        url = "https://api.aiforthai.in.th/ssense"
        data = {'text':sentence}
        headers = {
            'Apikey': "o5w87jBvYh7PiLfDbmKDtEoEb7DX7hqu"
            }
 
        response = requests.post(url, data=data, headers=headers)
        response_json = response.json()
        return JsonResponse({"student":"student_id", "sentimental":response_json}, safe=False)
    return JsonResponse({"error":"Method not allowed!"}, safe=False, status=403)
