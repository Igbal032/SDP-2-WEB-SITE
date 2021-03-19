from django.urls import path
# from .views import IndexPageView
# from .views import AboutPageView
from . import views

urlpatterns=[
    # path('',IndexPageView.as_view(),name="IndexPage"),
    # path('indexpg/<word>',views.ind),
    # path('about/<int:pk>/',AboutPageView.as_view(),name="AboutPage"),
    path('',views.home,name="home"),
    path('getSimiSenEmbe',views.getSimiSenEmbe,name="getSimiSenEmbe"),
    path('getVocabSenEmbe',views.getVocabSenEmbe,name="getVocabSenEmbe"),
    path('findSim',views.findSim,name="findSim"),
    path('findMostSim',views.findMostSim,name="findMostSim"),
]