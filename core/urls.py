from . import views
from django.urls import include, path

urlpatterns = [
    # localhost/cocktailbar/1
    path('cocktailbar/<int:id>', views.BarDetail.as_view()),
    # localhost/cocktailbar/all

    path('cocktailbar/all/', views.BarList.as_view()),
    path('cocktionary/<int:id>', views.CocktionaryDetail.as_view()),
    path('cocktionary/all', views.CocktionaryList.as_view()),
    #path('cocktionary/test', views.CocktionaryDetailViewTest.as_view()),
    #path('order/test', views.)
    path('cocktailbar/test', views.BarDetailImg.as_view()),
    ]

  

