from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details

from watchlist_app.api.views import ReviewDetail, WatchListAV, WatchDetailsAV, StreamPlatformAV, \
                                   StreamPlatformDetailsAV, ReviewList, ReviewCreate

urlpatterns = [

    path('list/', WatchListAV.as_view(), name='show-list'),
    path('<int:pk>/', WatchDetailsAV.as_view(), name='show-details'),

    path('platforms/', StreamPlatformAV.as_view(), name='platform-list'),
    path('platforms/<int:pk>/', StreamPlatformDetailsAV.as_view(), name='platform-details'),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='show-reviews'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='show-reviews'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    # path('review/', ReviewList.as_view(), name='review-list'),

    ]
