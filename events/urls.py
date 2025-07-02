from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, EventRegistrationViewSet


app_name = "events"

router = DefaultRouter()

router.register("events", EventViewSet)

router.register("registrations", EventRegistrationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
