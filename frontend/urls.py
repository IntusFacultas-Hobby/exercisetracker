from django.urls import path
from django.conf.urls import url
from .views import index_view

app_name = "frontend"

urlpatterns = [
    path('', index_view, name="frontend"),
    # regex matches, then lets routing be handled by the frontend. Still needs a / at end.
    url(r'^.*/$', index_view, name="frontend-router-catch")
]
