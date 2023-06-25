from django.shortcuts import render

from django.views import View
from django.http import JsonResponse, HttpResponse


import requests
# Create your views here.
class Word(View):
    def get(self, request):
        word = request.GET.get('word')
        if word:
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
            response = requests.get(url)
            response_json = response.json()
            cust_res = {}
            cust_res = response_json['word']
            cust_res = response_json['defenition']
            return JsonResponse(cust_res, safe=False)
        return HttpResponse('<h1>Enter a Word</h1>')