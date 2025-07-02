from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from events.models import Event, EventRegistration
from events.serializers import EventSerializer, EventRegistrationSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("location", "date")



class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
