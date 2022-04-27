from rest_framework.pagination import PageNumberPagination


class WatchListPagination(PageNumberPagination):
    page_size = 10


class StreamPlatformPagination(PageNumberPagination):
    page_size = 5


class ReviewListPagination(PageNumberPagination):
    page_size = 10
