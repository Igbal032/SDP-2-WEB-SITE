from django.urls import path
from . import views

urlpatterns=[
    # path('',IndexPageView.as_view(),name="IndexPage"),
    # path('indexpg/<word>',views.ind),
    # path('about/<int:pk>/',AboutPageView.as_view(),name="AboutPage"),
    path('',views.home,name="home"),
    path('SDP2',views.sdp2Page,name="SDP2"),
    path('SkipGram',views.SkipGramPage,name="SkipGram"),
    path('CBOW',views.CBOWPage,name="CBOW"),
    path('FastText',views.FastTextPage,name="FastText"),
    path('SenBytePair',views.SenBytePairPage,name="SenBytePair"),
    path('SenDoc2Vec',views.SenDoc2VecPage,name="SenDoc2Vec"),
    path('BertTokenizer',views.BertTokenizerPage,name="BertTokenizer"),



    
    path('getSimiSenEmbe',views.getSimiSenEmbe,name="getSimiSenEmbe"),
    path('getVocabSenEmbe',views.getVocabSenEmbe,name="getVocabSenEmbe"),
    path('findSim',views.findSim,name="findSim"),
    path('findMostSim',views.findMostSim,name="findMostSim"),
    path('findBertToken',views.findBertToken,name="findBertToken"),
]
