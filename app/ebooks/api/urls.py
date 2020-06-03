from django.urls import path

from ebooks.api.views import (EbookDetailAPIView, EbookListCreateAPIView,
                              ReviewCreateAPIView, ReviewDetailAPIView)

urlpatterns = [
    # Ebooks #
    path(
        'ebooks/',
        EbookListCreateAPIView.as_view(),
        name='ebook-list'
    ),
    path(
        'ebooks/<int:pk>/',
        EbookDetailAPIView.as_view(),
        name='ebook-detail'
    ),

    # Reviews #
    path(
        'ebooks/<int:ebook_pk>/reviews/',
        ReviewCreateAPIView.as_view(),
        name='review-list'
    ),
    path(
        'reviews/<int:pk>/',
        ReviewDetailAPIView.as_view(),
        name='rewview-detail'
    ),
]
