from django.urls import path
from . import views
#from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin

app_name = "polls"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.about, name="about"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

