from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from ebooks.api.pagination import SmallSetPagination
from ebooks.api.permissions import IsAdminUserOrReadOnly, IsAuthorOrReadOnly
from ebooks.api.serializers import EbookSerializer, ReviewSerializer
from ebooks.models import Ebook, Review


class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all().order_by('-id')
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get('ebook_pk')
        ebook = get_object_or_404(Ebook, pk=ebook_pk)

        author = self.request.user

        review_queryset = Review.objects.filter(ebook=ebook, author=author)
        if review_queryset.exists():
            raise ValidationError('You have already reviewed this ebook')

        return serializer.save(ebook=ebook, author=author)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthorOrReadOnly]
