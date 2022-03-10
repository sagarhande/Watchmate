from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details

from watchlist_app.api.views import WatchListAV, WatchDetailsAV, StreamPlatformAV, StreamPlatformDetailsAV
urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailsAV.as_view(), name='movie-details'),
    path('platforms/', StreamPlatformAV.as_view(), name='platform-list'),
    path('platforms/<int:pk>', StreamPlatformDetailsAV.as_view(), name='platform-details'),
    ]
