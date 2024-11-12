from django.shortcuts import render

from django.http import JsonResponse
from .elasticsearch_client import create_document, get_document, update_document, delete_document

def create_movie(request):
    doc = {
        'title': 'Inception',
        'director': 'Christopher Nolan',
        'year': 2010
    }
    response = create_document('movies', 1, doc)
    return JsonResponse(response)

def get_movie(request):
    movie = get_document('movies', 1)
    return JsonResponse(movie)

def update_movie(request):
    updated_fields = {
        'year': 2011
    }
    response = update_document('movies', 1, updated_fields)
    return JsonResponse(response)

def delete_movie(request):
    response = delete_document('movies', 1)
    return JsonResponse(response)
