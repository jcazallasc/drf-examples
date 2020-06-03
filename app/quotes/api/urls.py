from django.urls import path

from quotes.api.views import QuoteDetailCreateAPIView, QuoteListCreateAPIView

urlpatterns = [
    path(
        'quotes/',
        QuoteListCreateAPIView.as_view(),
        name='quote-list'
    ),
    path(
        'quotes/<int:pk>/',
        QuoteDetailCreateAPIView.as_view(),
        name='quote-detail'
    ),
]
