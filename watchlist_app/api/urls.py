from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details

from watchlist_app.api.views import ReviewDetail, WatchListGV, WatchDetailsGV, StreamPlatformGV, \
                                   StreamPlatformDetailsGV, ReviewList, ReviewCreate, UserReview

urlpatterns = [

    path('list/', WatchListGV.as_view(), name='show-list'),
    path('<int:pk>/', WatchDetailsGV.as_view(), name='show-details'),

    path('platforms/', StreamPlatformGV.as_view(), name='platform-list'),
    path('platforms/<int:pk>/', StreamPlatformDetailsGV.as_view(), name='platform-details'),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='create-show-reviews'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='show-reviews-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('reviews/', UserReview.as_view(), name='user-review-list'),

    ]
