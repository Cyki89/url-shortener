from django.shortcuts import get_object_or_404, redirect
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import UrlShortener
from .serializers import UrlShortenerSerializer


def redirect_view(request, short_code):
    url_model = get_object_or_404(UrlShortener, short_code=short_code)
    return redirect(url_model.full_url)


class UrlShortenerViewSet(RetrieveModelMixin, CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = UrlShortener.objects.all()
    serializer_class = UrlShortenerSerializer
    lookup_field = 'short_code'