from rest_framework import generics

from quotes.api.pagination import BasicSetPagination
from quotes.api.permissions import IsAdminUserOrReadOnly
from quotes.api.serializers import QuoteSerializer
from quotes.models import Quote


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by('-id')
    serializer_class = QuoteSerializer
    pagination_class = BasicSetPagination
    permission_classes = [IsAdminUserOrReadOnly]


class QuoteDetailCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
