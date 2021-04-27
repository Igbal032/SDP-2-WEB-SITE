from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('SDP2',views.sdpPage,name="SDP2"),
    path('SkipGram',views.SGW2VPage,name="SkipGram"),
    path('CBOW',views.CBOWW2VPage,name="CBOW"),
    path('FastText',views.CBOWFTPage,name="FastText"),
    path('SGFastText',views.SGFTPage,name="SGFastText"),
    path('Authors',views.AuthorsPage,name="Authors"),
    
    
    path('findSim',views.findSim,name="findSim"),
    path('findMostSim',views.findMostSim,name="findMostSim"),
    path('findAnalogy',views.findAnalogy,name="findAnalogy"),
]
