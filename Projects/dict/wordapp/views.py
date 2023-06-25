from django.shortcuts import render

from django.views import View
from django.http import JsonResponse


import requests
# Create your views here.
class Word(View):
    def get(request):
        word = request.GET.get(word)
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        return JsonResponse(response)