from rest_framework.pagination import PageNumberPagination


class BasicSetPagination(PageNumberPagination):
    page_size = 30
