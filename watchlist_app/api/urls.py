from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details

from watchlist_app.api.views import ReviewDetail, WatchListAV, WatchDetailsAV, StreamPlatformAV, StreamPlatformDetailsAV, ReviewList
urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailsAV.as_view(), name='movie-details'),
    path('platforms/', StreamPlatformAV.as_view(), name='platform-list'),
    path('platforms/<int:pk>', StreamPlatformDetailsAV.as_view(), name='platform-details'),

    path('review', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    ]
