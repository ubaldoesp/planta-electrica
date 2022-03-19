from django.urls import path, include


urlpatterns = [
    path("api/", include("bitacora.api.urls")),
]
