from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details

from watchlist_app.api.views import MovieListAV, MovieDetailsAV
urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailsAV.as_view(), name='movie-details')
    ]
