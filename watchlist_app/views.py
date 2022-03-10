# from django.shortcuts import render
# from watchlist_app import models
# from rest_framework.response import Response
# from django.http import JsonResponse
#
#
# # Create your views here.
# def movie_list(request):
#     movies = list(models.Movie.objects.all().values())
#     return JsonResponse({'movies': movies})
#
# 
# def movie_details(request, pk):
#     movie = models.Movie.objects.get(pk=pk)
#     data = {
#         'name': movie.name,
#         'description': movie.description,
#         'active': movie.active,
#         }
#     return JsonResponse(data)
