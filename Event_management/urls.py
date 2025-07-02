from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "auth/",
        include("djoser.urls")
    ),

    path(
        "auth/",
        include("djoser.urls.authtoken")
    ),

    path(
        "api/doc/",
        SpectacularAPIView.as_view(),
        name="schema"
    ),

    path(
        "api/doc/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger_ui"
    ),

    path(
        "api/doc/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc"
    ),

    path(
        "api/events/",
        include("events.urls"),
        name="events"
    ),
]
