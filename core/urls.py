from . import views
from .views import BarDetail
from django.urls import include, path

urlpatterns = [
    # localhost/cocktailbar/1
    path('<int:id>', views.BarDetail.as_view()),
    # localhost/cocktailbar/all
    path('all/', views.BarList.as_view()),
    ]
